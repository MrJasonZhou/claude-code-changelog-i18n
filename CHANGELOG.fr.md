# Journal des modifications de Claude Code (traduction française non officielle)

> Unofficial translation of the [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md). Not affiliated with Anthropic. Original © Anthropic PBC. Machine-translated; the English original is authoritative.

## 2.1.294 (2026-10-08)

- Correction des hooks `prompt` et `agent` rédigés sous forme d'instructions (comme "Bloquer les commandes qui...") qui autorisaient ce qu'ils devaient bloquer
- Amélioration de l'évaluation des hooks `prompt` sur Stop et SubagentStop rédigés sous forme d'instructions (comme "Continuer si le build est cassé"), afin que Claude soit moins susceptible de s'arrêter prématurément
