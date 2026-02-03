---
name: workflow-validation
description: Skill for static validation of workflows, ensuring integrity and safety without execution.
allowed-tools: Read, Grep, Bash
---

# Workflow Validation

> "Trust, but verify (statically)."

## 1. Principles
- **Static Analysis**: Do not run the code. Read it.
- **Link Integrity**: If a workflow says "Use agent X", agent X must exist.
- **Syntax Safety**: Catch typos before they crash the runtime.

## 2. Scripts Disponíveis

| Script | Propósito | Comando |
|--------|-----------|---------|
| Validate Syntax | Verifica sintaxe python e integridade de links | `python .agent/skills/workflow-validation/scripts/validate_syntax.py [path/to/workflow.md_or_dir]` |

## 3. Usage Examples

### Validate specific workflow
```bash
python .agent/skills/workflow-validation/scripts/validate_syntax.py .agent/workflows/forge.md
```
