#!/usr/bin/env python3
"""Translate new Claude Code CHANGELOG entries with agy, then rebuild CHANGELOG.<lang>.md.

Safe to run repeatedly (cron): finished translations are cached in i18n/<lang>/<version>.md
keyed by a hash of the English text. Any agy failure (e.g. quota) stops the run; the next
run picks up where this one left off.
"""
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import urllib.request

SINCE = os.environ.get('SINCE', '2026-08-08')  # versions published on/after this date; move back to backfill
MODEL = 'gemini-3.8-flash-medium'
WORKERS = 4
CHANGELOG_URL = 'https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md'
NPM_URL = 'https://registry.npmjs.org/@anthropic-ai/claude-code'
LANGS = {
    'zh-CN': 'Simplified Chinese',
    'zh-TW': 'Traditional Chinese (Taiwan)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'pt-BR': 'Brazilian Portuguese',
}
HEADER = {
    'zh-CN': '# Claude Code 更新日志（非官方简体中文翻译）',
    'zh-TW': '# Claude Code 更新日誌（非官方繁體中文翻譯）',
    'ja': '# Claude Code 変更履歴（非公式日本語訳）',
    'ko': '# Claude Code 변경 로그 (비공식 한국어 번역)',
    'fr': '# Journal des modifications de Claude Code (traduction française non officielle)',
    'de': '# Claude Code Changelog (inoffizielle deutsche Übersetzung)',
    'es': '# Registro de cambios de Claude Code (traducción no oficial al español)',
    'pt-BR': '# Changelog do Claude Code (tradução não oficial para português do Brasil)',
}
PROMPT = """Translate the following Claude Code release notes from English into {lang}.
Rules:
- This is a pure text translation task. Do NOT use any tools, run commands, or read files.
- Output ONLY the translated Markdown, nothing else (no preamble, no code fences around the whole output).
- Keep the exact Markdown structure: same bullets, same order, same line count.
- Do NOT translate anything inside backticks, command names, CLI flags, file paths, env vars, product names (Claude Code, Claude, MCP, VS Code, etc.) or URLs.
- Use natural, concise technical wording that developers in that language would use.

{text}"""

ROOT = os.path.dirname(os.path.abspath(__file__))
stop = threading.Event()
lock = threading.Lock()
failures = [0]  # consecutive agy failures
MAX_FAILURES = 3


def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode()


def parse(md):
    """Return [(version, body)] in CHANGELOG order."""
    parts = re.split(r'^## (\S+)\s*$', md, flags=re.M)
    return [(parts[i], parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def digest(text):
    return hashlib.sha1(text.encode()).hexdigest()[:12]


def bullets(text):
    return sum(line.lstrip().startswith('- ') for line in text.splitlines())


def cache_path(lang, ver):
    return os.path.join(ROOT, 'i18n', lang, ver + '.md')


def cached(lang, ver, h):
    try:
        with open(cache_path(lang, ver)) as f:
            return f.readline().strip() == f'<!-- src:{h} -->'
    except FileNotFoundError:
        return False


def translate(lang, ver, body, h):
    if stop.is_set():
        return
    with tempfile.TemporaryDirectory() as cwd:  # ponytail: empty cwd so the agent has nothing to touch
        p = subprocess.run(
            ['agy', '--output-format', 'json', '--print-timeout', '300s', '--disable-slash-commands',
             '--model', MODEL, '-p=' + PROMPT.format(lang=LANGS[lang], text=body)],
            cwd=cwd, capture_output=True, text=True)
    try:
        out = json.loads(p.stdout)
    except ValueError:
        out = {}
    text = (out.get('response') or '').strip()
    if bullets(text) != bullets(body):  # truncated or merged lines; retry next run
        text = ''
    if p.returncode or out.get('status') != 'SUCCESS' or not text:
        with lock:
            failures[0] += 1
            if failures[0] >= MAX_FAILURES:  # ponytail: repeated failures ~= quota hit; no way to tell for sure
                stop.set()
        print(f'agy failed on {ver} {lang}: rc={p.returncode} {(p.stdout + p.stderr)[-500:]}', file=sys.stderr)
        return
    with lock:
        failures[0] = 0
    os.makedirs(os.path.dirname(cache_path(lang, ver)), exist_ok=True)
    with open(cache_path(lang, ver), 'w') as f:
        f.write(f'<!-- src:{h} -->\n{text}\n')
    print(f'ok {ver} {lang}')


def build(lang, entries, dates):
    lines = [HEADER[lang], '',
             '> Unofficial translation of the [Claude Code CHANGELOG]'
             '(https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). '
             'Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; '
             'the English original is authoritative.', '']
    for ver, _ in entries:
        if not os.path.exists(cache_path(lang, ver)):
            continue
        with open(cache_path(lang, ver)) as f:
            text = f.read().split('\n', 1)[1].strip()
        lines += [f'## {ver}' + (f' ({dates[ver][:10]})' if ver in dates else ''), '', text, '']
    with open(os.path.join(ROOT, f'CHANGELOG.{lang}.md'), 'w') as f:
        f.write('\n'.join(lines))


def main():
    entries = parse(fetch(CHANGELOG_URL))
    dates = json.loads(fetch(NPM_URL))['time']
    todo = [(lang, ver, body, digest(body))
            for ver, body in entries if dates.get(ver, '') >= SINCE and body
            for lang in LANGS]
    todo = [t for t in todo if not cached(t[0], t[1], t[3])]
    print(f'{len(todo)} translations to do')
    with concurrent.futures.ThreadPoolExecutor(WORKERS) as ex:
        list(ex.map(lambda t: translate(*t), todo))
    for lang in LANGS:
        build(lang, entries, dates)
    return 75 if stop.is_set() else 0  # 75 = EX_TEMPFAIL, retry next run


if __name__ == '__main__':
    sys.exit(main())
