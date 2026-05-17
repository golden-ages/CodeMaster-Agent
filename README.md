# CodeMaster-Agent

CodeMaster-Agent is a local, multi-agent collaborative system designed for codebase architecture refactoring and automated documentation generation. It helps developers safely manage technical debt in legacy Python projects.

## Core Architecture
1. Parser Agent: Constructs an Abstract Syntax Tree (AST) to map global dependencies.
2. Tech-Debt Agent: Scans for high coupling and undocumented functions.
3. Refactor Agent: Generates decoupled code and synthesizes API documentation.

## Setup
Clone the repository and install dependencies:
pip install -r requirements.txt

## Usage
Run the main pipeline against a target directory:
python main.py --target ./test_project