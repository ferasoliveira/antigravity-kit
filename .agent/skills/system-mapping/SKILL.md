---
name: system-mapping
description: Skill for discovering and mapping the .agent system structure. Used to list agents/skills and visualize dependencies.
allowed-tools: Read, Glob, Grep, Bash, Write
---

# System Mapping & Discovery

> Tools to understand the existing `.agent` ecosystem and prevent duplication.

## 1. Principles
- **Discovery First**: Always check if an agent/skill exists before designing a new one.
- **Semantic Mapping**: Understand not just the filename, but the purpose of the agent.
- **Dependency Awareness**: Know which agents use which skills.

## 2. Scripts Disponíveis

| Script | Propósito | Comando |
|--------|-----------|---------|
| Registry Updater | Atualiza/Lista índices do sistema | `python .agent/skills/system-mapping/scripts/registry_updater.py` |
| Visualize Workflow | Gera diagrama Mermaid de workflows | `python .agent/skills/system-mapping/scripts/visualize_workflow.py [path/to/workflow.md]` |

## 3. Usage Examples

### List all agents
```bash
python .agent/skills/system-mapping/scripts/registry_updater.py --list-agents
```

### Visualize a workflow
```bash
python .agent/skills/system-mapping/scripts/visualize_workflow.py .agent/workflows/deploy.md
```
