import sys
import os
import re

def parse_workflow(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    steps = []
    # Simple heuristic to find numbered steps
    # Looks for lines starting with "1. **Title**" or just "1. Step"
    pattern = re.compile(r'^\d+\.\s+(?:\*\*(.*?)\*\*|(.*))', re.MULTILINE)
    
    matches = pattern.findall(content)
    for match in matches:
        # match is a tuple, take the non-empty group
        step_text = match[0] if match[0] else match[1]
        steps.append(step_text.strip())
        
    return steps

def generate_mermaid(name, steps):
    print("```mermaid")
    print("graph TD")
    print(f"    subgraph {name}")
    print("    Start((Start))")
    
    last_node = "Start"
    for i, step in enumerate(steps):
        node_id = f"Step{i+1}"
        # Escape quotes for mermaid
        sanitized_step = step.replace('"', "'")
        print(f'    {node_id}["{sanitized_step}"]')
        print(f"    {last_node} --> {node_id}")
        last_node = node_id
        
    print("    End((End))")
    print(f"    {last_node} --> End")
    print("    end")
    print("```")

def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize_workflow.py <path_to_workflow.md>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    name = os.path.basename(file_path).replace('.md', '')
    
    try:
        steps = parse_workflow(file_path)
        if not steps:
            print("No steps found or could not parse steps.")
            return
            
        generate_mermaid(name, steps)
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")

if __name__ == "__main__":
    main()
