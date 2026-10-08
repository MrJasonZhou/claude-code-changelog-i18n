# Claude Code Changelog (inoffizielle deutsche Übersetzung)

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- Fehler behoben, bei dem als Anweisungen formulierte `prompt`- und `agent`-Hooks (wie "Block commands that...") das zuließen, was sie blockieren sollten
- Auswertung von als Anweisungen formulierten `prompt`-Hooks für Stop und SubagentStop (wie "Carry on if the build is broken") verbessert, sodass Claude seltener vorzeitig stoppt
