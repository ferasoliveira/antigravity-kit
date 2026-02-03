import os
import argparse
import sys

AGENT_ROOT = os.path.join(os.getcwd(), '.agent')
AGENTS_DIR = os.path.join(AGENT_ROOT, 'agents')
SKILLS_DIR = os.path.join(AGENT_ROOT, 'skills')

def list_files(directory, ext=".md"):
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith(ext)]

def list_subdirs(directory):
    if not os.path.exists(directory):
        return []
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def main():
    parser = argparse.ArgumentParser(description="Registry Updater & Lister")
    parser.add_argument("--list-agents", action="store_true", help="List all available agents")
    parser.add_argument("--list-skills", action="store_true", help="List all available skills")
    
    args = parser.parse_args()
    
    if args.list_agents:
        agents = list_files(AGENTS_DIR)
        print("Existing Agents:")
        for agent in agents:
            print(f" - {agent.replace('.md', '')}")
            
    if args.list_skills:
        skills = list_subdirs(SKILLS_DIR)
        print("\nExisting Skills:")
        for skill in skills:
            print(f" - {skill}")

if __name__ == "__main__":
    main()
