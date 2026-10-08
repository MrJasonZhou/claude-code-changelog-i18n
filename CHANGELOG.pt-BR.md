# Changelog do Claude Code (tradução não oficial para português do Brasil)

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- Corrigidos hooks de `prompt` e `agent` escritos como instruções (como "Bloquear comandos que...") que permitiam o que deveriam bloquear
- Melhorada a forma como hooks de `prompt` em Stop e SubagentStop escritos como instruções (como "Continuar se o build quebrar") são avaliados, reduzindo a chance de o Claude parar prematuramente
