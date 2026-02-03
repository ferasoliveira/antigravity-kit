---
name: meta-programming
description: Skill for dynamic template manipulation and file generation. Required for creating new agents, skills, and workflows programmatically.
allowed-tools: Read, Write, Edit, Glob
---

# Meta Programming

> "Code that writes code."

## 1. Principles
- **Dynamic Templates**: Never hardcode. Use `instrucoes.md` as the source of truth for templates.
- **Safe Injection**: When modifying files (like `skills:` list), always use parsing/regex, never append blindly.
- **Validation**: Generated code must be syntactically valid.
- **Rich Content**: generated files *must not* be abstract summaries. They must contain concrete examples, code snippets, and specific rules.
- **System Metrics**: A robust system typically requires at least **2 Agents** (Separation of Concerns) and **3 Skills** (Modular Knowledge).

## 2. Key Operations

### Dynamic Template Loading
The `Forge Master` should read `instrucoes.md` to extract the latest templates for Agents and Skills.

### Frontmatter Manipulation
Use safe string replacement or YAML parsers to update `skills:` fields in existing agents.

## 3. Scripts
*No specific scripts yet. Logic resides within the Forge Master's instructions.*
