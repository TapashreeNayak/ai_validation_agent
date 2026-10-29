# Run the application using below command:

# powershell

python le_validation_agent.py LegalEntity_Sample.xlsx --sheet Legal_Entity --output validation_report.xlsx

# Command Prompt

python le_validation_agent.py LegalEntity_Sample.xlsx \
 --sheet Legal_Entity \
 --output validation_report.xlsx

# Install below dependencies to run this application

python -m pip install langchain-chroma langchain-community langchain-huggingface chromadb sentence-transformers

pip install tenacity pybreaker

# KnowledgeBase Details

1. FRC_Data_Validation_Standard.md
   Defines validation rules, what each error means, and what an analyst should do. This is the primary source for retrieving explanations for errors such as DUPLICATE_CODE, INVALID_STATUS, and UNKNOWN_PARENT.

2. FRC_Data_Maintenance_Procedure.md

Describes the approved process for correcting reference data, including who can approve changes, when to escalate, and why the AI must not invent replacement values.

3. FRC_Reference_Mappings.csv

Contains approved reference values, such as valid statuses, country codes, and component mappings. Use this for exact lookups as well as RAG where appropriate.

4. FRC_Hierarchy_Rules.md

Explains parent-child relationships, whether parent references are mandatory, and how to handle unknown or self-referencing parents.
