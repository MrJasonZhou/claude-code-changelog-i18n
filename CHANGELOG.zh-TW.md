# Claude Code 更新日誌（非官方繁體中文翻譯）

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- 修復以指示形式撰寫的 `prompt` 與 `agent` hook（例如 "Block commands that..."）放行了本應阻擋內容的問題
- 改善以指示形式撰寫於 Stop 與 SubagentStop 的 `prompt` hook（例如 "Carry on if the build is broken"）之判定機制，降低 Claude 過早停止的機率
