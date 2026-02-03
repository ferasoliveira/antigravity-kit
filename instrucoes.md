# Instruções para Adicionar Agentes, Skills e Workflows (.agent)

Este documento descreve como estender o sistema existente na pasta `.agent`, adicionando novos agentes, habilidades (skills) e fluxos de trabalho (workflows).

---

## 📂 Estrutura de Diretórios

O sistema segue a seguinte estrutura dentro de `.agent`:

```text
.agent/
├── agents/            # Definições dos Agentes (.md)
├── skills/            # Habilidades modulares (pastas com SKILL.md)
│   ├── [nome-skill]/
│   │   ├── SKILL.md
│   │   └── scripts/   # Scripts auxiliares (.py, .sh)
├── workflows/         # Comandos Slash (/comando) (.md)
└── scripts/           # Scripts globais (opcional)
```

---

## 1. Adicionando Agentes (`agents/`)

Agentes são personas especializadas. Cada agente é um arquivo Markdown único.

### 📍 Localização
Salve o arquivo em: `.agent/agents/[nome-do-agente].md`

### 📝 Template de Agente

```markdown
---
name: [nome-do-agente]
description: [Uma frase descrevendo o propósito. Ex: Especialista em banco de dados.]
tools: Read, Grep, Glob, Bash, Write, Edit, Agent
model: inherit
skills: [lista-de-skills-separada-por-virgula]
---

# [Nome Completo do Agente]

[Definição da Persona: Quem é o agente, suas prioridades e estilo de comunicação.]

## Funções Principais
- Função 1
- Função 2

## Regras de Atuação
1. **Regra 1**: Descrição.
2. **Regra 2**: Descrição.

## Limites (Onde NÃO atuar)
- Não deve fazer X.
- Não deve fazer Y.

## Protocolo de Atuação
Passos que o agente deve seguir ao receber uma tarefa.
```

### 💡 Dicas para Agentes
- **skills**:liste apenas os nomes das pastas dentro de `.agent/skills` que este agente deve carregar (ex: `clean-code, python-patterns`).
- **tools**: Geralmente mantenha o padrão listado no template.

---

## 2. Adicionando Skills (`skills/`)

Skills são conjuntos de conhecimento e ferramentas modulares. Elas ficam em subpastas próprias.

### 📍 Localização
1. Crie uma pasta: `.agent/skills/[nome-da-skill]/`
2. Crie o arquivo principal: `.agent/skills/[nome-da-skill]/SKILL.md`

### 📝 Template de Skill (`SKILL.md`)

```markdown
---
name: [nome-da-skill]
description: [Descrição breve do que a skill ensina ou fornece.]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# [Título da Skill]

> [Subtítulo ou resumo breve]

## 1. Princípios
Conceitos fundamentais que o agente deve entender.

## 2. Padrões
Exemplos de código ou procedimentos recomendados.

## 3. Comandos Úteis
Tabelas ou listas de comandos relacionados à skill.

```

### 🔗 Integrando Scripts em Skills
Se a skill precisa executar scripts (Python, Bash, etc.):

1. Crie uma pasta `scripts` dentro da pasta da skill:
   `.agent/skills/[nome-da-skill]/scripts/`
2. Coloque seus scripts lá (ex: `audit.py`).
3. No arquivo `SKILL.md`, instrua o agente sobre como usar o script:

```markdown
## Scripts Disponíveis

| Script | Propósito | Comando |
|--------|-----------|---------|
| Audit | Audita X | `python .agent/skills/[nome-da-skill]/scripts/audit.py` |
```

**Importante:** Sempre use o caminho relativo a partir da raiz do projeto (`.agent/...`) ao documentar o comando.

---

## 3. Adicionando Workflows (`workflows/`)

Workflows definem processos passo-a-passo disparados por comandos slash (ex: `/deploy`).

### 📍 Localização
Salve o arquivo em: `.agent/workflows/[nome-do-comando].md` (ex: `deploy.md` para o comando `/deploy`).

### 📝 Template de Workflow

```markdown
---
description: [Descrição curta do que o comando faz]
---

# /[nome-do-comando] - [Título Descritivo]

$ARGUMENTS

---

## Objetivo
Descreva o que este workflow realiza.

## Passos de Execução

1. **Passo 1**: Faça X.
2. **Passo 2**: Verifique Y.
3. **Passo 3**: Se necessário, chame o agente Z:
   > "Use o agente [nome-do-agente] para realizar [tarefa]..."

## Exemplo de Uso
/comando argumento1
```

### 💡 Dicas para Workflows
- **$ARGUMENTS**: O sistema substitui isso pelos argumentos passados pelo usuário.
- **Turbo Mode**: Se quiser que um passo rode automaticamente sem confirmação (apenas `run_command`), adicione `// turbo` na linha anterior ao passo.

---

## Resumo do Processo de Integração

1. **Planeje**: O que você precisa? Uma nova persona (Agente)? Um conhecimento específico (Skill)? Ou um processo (Workflow)?
2. **Crie os Arquivos**: Siga os templates acima.
3. **Conecte**:
   - Se criou uma **Skill**, adicione o nome dela no frontmatter `skills:` dos **Agentes** que precisam dela.
   - Se criou um **Workflow**, ele pode invocar **Agentes** específicos.
   - Se criou um **Script**, coloque-o na pasta da **Skill** correspondente e documente o comando no `SKILL.md`.
