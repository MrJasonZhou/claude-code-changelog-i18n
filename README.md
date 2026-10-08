# Claude Code Changelog i18n

Unofficial translations of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), updated automatically within about an hour of each release.

| Language | File |
|---|---|
| 简体中文 | [CHANGELOG.zh-CN.md](CHANGELOG.zh-CN.md) |
| 繁體中文 | [CHANGELOG.zh-TW.md](CHANGELOG.zh-TW.md) |
| 日本語 | [CHANGELOG.ja.md](CHANGELOG.ja.md) |
| 한국어 | [CHANGELOG.ko.md](CHANGELOG.ko.md) |
| Français | [CHANGELOG.fr.md](CHANGELOG.fr.md) |
| Deutsch | [CHANGELOG.de.md](CHANGELOG.de.md) |
| Español | [CHANGELOG.es.md](CHANGELOG.es.md) |
| Português (Brasil) | [CHANGELOG.pt-BR.md](CHANGELOG.pt-BR.md) |

Coverage currently starts from versions released on or after 2026-08-08; older versions will be added over time.

## Disclaimer

- This is an **unofficial** community project and is **not affiliated with or endorsed by Anthropic**.
- The original CHANGELOG is © Anthropic PBC, all rights reserved. Translations are provided for reference only; the English original is authoritative.
- Translations are machine-generated and may contain errors. Corrections via issues or pull requests are welcome.
- If you are a rights holder and want this repository taken down, please open an issue and it will be removed promptly.

## How it works

`run.sh` runs hourly: `translate.py` fetches the upstream CHANGELOG and npm release dates, translates each new version × language with an LLM, caches results in `i18n/<lang>/<version>.md` (keyed by a hash of the English text, so upstream edits get retranslated), then rebuilds the `CHANGELOG.<lang>.md` files and pushes.
