# Claude Code 変更履歴（非公式日本語訳）

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- 指示（「…するコマンドをブロック」など）として記述された `prompt` および `agent` フックが、ブロックすべき対象を許可してしまう問題を修正
- Stop および SubagentStop において指示（「ビルドが失敗しても続行」など）として記述された `prompt` フックの判定を改善し、Claude が早期に停止しにくくしました
