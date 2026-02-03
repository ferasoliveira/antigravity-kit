---
description: Advanced workflow to create complex Agent Architectures (Agents + Skills + Scripts). Focuses on depth and automation.
---

# /forge-agent - Deep Agent Architecture

$ARGUMENTS

---

## Purpose
The `/forge-agent` command focuses exclusively on designing and building **Robust Autonomous Agents**. It does not create slash commands. It creates specialized Personas, deep Knowledge Bases (Skills), and Automation Utilities (Scripts).

## Execution Flow

1.  **Domain Discovery**
    > **System Architect** analyzes the domain.
    - Runs `system-mapping` to see existing agents.
    - Socratic Gate: Asks about the specific Role and Responsibilities.

2.  **Structural Deepening (MVS Phase)**
    > **System Architect** designs the MVS (Minimum Viable System).
    - **Constraint**: Must design at least **2 Agents** (e.g., Worker + Supervisor).
    - **Constraint**: Must design at least **3 Skills** with "Rich Content".
    - **Constraint**: Must design at least **1 Automation Script** (Python) for the skills.
    
    - Output: `.agent/.internal/plans/PLAN-agent-[name].md` (Internal).

3.  **Fabrication**
    > **Forge Master** generates files.
    - Creates Agents, Skills, and **Scripts**.
    - Enforces "Rich Content" (rejects shallow files).

4.  **Registration**
    > **Forge Master** registers components.
    - Runs `registry_updater.py`.

5.  **Validation**
    > **System Architect** runs syntax checks.

## Usage Example
```
/forge-agent "Create a Crypto Trading Bot that analyzes sentiment and executes orders"
```
