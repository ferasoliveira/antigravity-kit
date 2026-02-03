---
description: Create new Agents, Skills, and Workflows automatically using the Meta-Builder system.
---

# /forge - Meta-Builder Workflow

$ARGUMENTS

---

## Purpose
The `/forge` command initiates the "Genesis" process to create new system components (Agents, Skills, Workflows) based on natural language descriptions.

## Execution Flow

1.  **Discovery & Socratic Gate**
    > **System Architect** analyzes request.
    - Run `registry_updater.py` to map current system.
    - Ask 3 questions to clarify intent (Socratic Gate).
    - Checks for duplication.

2.  **Structural Deepening**
    > **System Architect** expands the scope.
    - **Enforce MVS**: Ensure design has at least 2 Agents and 3 Skills.
    - **Detailing**: Expand generic requirements into specific sections/examples for the Blueprint.
    - Output: `.agent/.internal/plans/PLAN-forge-[name].md` (Internal).
    - *Note*: Visible plan created only if requested.

3.  **Fabrication**
    > **Forge Master** generates files.
    - Reads `instrucoes.md`.
    - Generates `.md` and `.py` files using **Dynamic Templates**.

4.  **Routing & Registration**
    > **Forge Master** registers components.
    - Ensure `registry_updater.py` is run to index new agents.

5.  **Static Validation**
    > **System Architect** verifies integrity.
    - Run `validate_syntax.py` on new files.
    - Verify link integrity.

## Usage Example
```
/forge "Create a market analysis agent that uses Yahoo Finance API"
```
