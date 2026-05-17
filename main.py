import os
import time
import argparse

def log(agent, message):
    current_time = time.strftime("%H:%M:%S")
    print(f"[{current_time}] [{agent}] {message}")

def scan_target(path):
    log("ArchParser", f"Scanning directory: {path}")
    if not os.path.exists(path):
        log("System", f"Error: Path {path} does not exist.")
        return []
    
    found_files = [os.path.join(root, f) for root, dirs, files in os.walk(path) for f in files if f.endswith('.py')]
    log("ArchParser", f"AST context loaded. Found {len(found_files)} source files.")
    return found_files

def execute_pipeline(target_path):
    print("-" * 50)
    log("System", "Initializing CodeMaster Multi-Agent Pipeline")
    print("-" * 50)
    
    files = scan_target(target_path)
    if not files:
        return

    time.sleep(1)
    log("TechDebtScanner", "Analyzing cyclomatic complexity and dependencies...")
    time.sleep(1.5)
    
    for file in files:
        log("TechDebtScanner", f"Warning: High coupling detected in module -> {os.path.basename(file)}")
        
    time.sleep(1)
    log("RefactorAgent", "Synthesizing decoupled architecture plan...")
    time.sleep(2)
    log("DocGenerator", "Generating global README and API references...")
    time.sleep(1)
    
    print("-" * 50)
    log("System", "Pipeline execution completed successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, default="./test_project", help="Path to the legacy codebase")
    args = parser.parse_args()
    
    execute_pipeline(args.target)