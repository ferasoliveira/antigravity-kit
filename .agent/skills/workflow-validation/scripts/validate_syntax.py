import os
import argparse
import re

AGENT_ROOT = os.path.join(os.getcwd(), '.agent')
AGENTS_DIR = os.path.join(AGENT_ROOT, 'agents')
WORKFLOWS_DIR = os.path.join(AGENT_ROOT, 'workflows')

def get_existing_agents():
    if not os.path.exists(AGENTS_DIR):
        return set()
    return {f.replace('.md', '') for f in os.listdir(AGENTS_DIR) if f.endswith('.md')}

def validate_workflow_links(file_path, existing_agents):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Heuristic: Find mentions of agents in quotes or code blocks
    # e.g. "Use the agent `market-watcher`" or "Invoke market-watcher"
    # This is a loose check.
    
    errors = []
    
    # Regex to find potential agent names (simplified)
    # Looking for words that look like agents (lowercase, hyphenated)
    potential_agents = re.findall(r'`([a-z0-9-]+)`', content)
    
    for agent in potential_agents:
        # Ignore common non-agent terms if any, but for now check all
        # Optimization: Only check if it looks like an agent in the context of "agent `name`"
        if agent in existing_agents:
            continue
        
        # If it's not a known agent, is it a false positive?
        # We can't be sure without NLP, so we'll just warn if it looks very agent-like
        # but isn't in the list.
        # For this script, let's strictly look for specific phrases if possible.
        pass

    return errors

def validate_file_structure(path):
    # Basic check: does file exist and is not empty
    if not os.path.exists(path):
        return f"File not found: {path}"
    if os.path.getsize(path) == 0:
        return f"File is empty: {path}"
    return None

def main():
    parser = argparse.ArgumentParser(description="Workflow Static Validator")
    parser.add_argument("path", help="Path to file or directory to validate")
    
    args = parser.parse_args()
    target = args.path
    
    issues = []
    
    if os.path.isfile(target):
        err = validate_file_structure(target)
        if err: issues.append(err)
        # Add more logic here
    elif os.path.isdir(target):
         for root, _, files in os.walk(target):
            for file in files:
                if file.endswith('.md'):
                    err = validate_file_structure(os.path.join(root, file))
                    if err: issues.append(err)

    if issues:
        print("Validation Issues Found:")
        for i in issues:
            print(f" - {i}")
        sys.exit(1)
    else:
        print("Validation Passed (Basic Structure).")

if __name__ == "__main__":
    import sys
    main()
