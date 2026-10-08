# Claude Code 변경 로그 (비공식 한국어 번역)

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- 지시문 형태(예: "Block commands that...")로 작성된 `prompt` 및 `agent` 훅이 차단해야 할 대상을 허용하던 문제 수정
- Stop 및 SubagentStop에서 지시문 형태(예: "Carry on if the build is broken")로 작성된 `prompt` 훅의 평가 방식을 개선하여 Claude가 조기에 중단될 가능성을 낮춤
