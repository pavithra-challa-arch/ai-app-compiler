# AI App Compiler

## Project Overview
This project is an AI-powered system that converts natural language input into a structured application schema.

It behaves like a compiler for software generation:
Natural Language → Intent → System Design → Schema Generation → Validation → Repair → Final Output


## Features
- Intent Extraction from user input
- System Design generation (entities, roles, flows)
- UI, API, Database schema generation
- Authentication and role-based access
- Validation system for schema correctness
- Auto-repair mechanism for missing fields


## Tech Used
- Python
- Rule-based AI logic
- Modular pipeline architecture



## How it works
1. User gives input (e.g., "Build CRM with login and dashboard")
2. System extracts intent
3. Creates system design
4. Generates full application schema
5. Validates output
6. Repairs missing parts if needed
7. Outputs final JSON schema



## How to Run
cd backend
python main.py
