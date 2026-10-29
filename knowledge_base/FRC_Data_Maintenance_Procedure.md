# FRC Data Maintenance Procedure

Document ID: FRC-PROC-001
Version: 1.0
Status: DEMO_APPROVED
Owner: Reference Data Governance

## Procedure 1: Investigate a validation failure

1. Review the deterministic validation message.
2. Identify the affected record and field.
3. Retrieve the applicable validation rule.
4. Check approved reference mappings when relevant.
5. Propose a correction only when supported by approved evidence.
6. Otherwise, request confirmation from the authorized data owner.

## Procedure 2: Change reference data

1. Identify the source record and proposed change.
2. Record the reason for the proposed change.
3. Obtain approval from the designated data owner.
4. Apply the change through the authorized maintenance process.
5. Re-run validation after the change.
6. Retain the original value, updated value, approval,
   and validation result in the audit trail.

## AI assistant restrictions

The AI assistant may explain errors and suggest next steps.

The AI assistant must not:

- Modify the source workbook automatically.
- Invent a missing component name.
- Delete a duplicate record without authorization.
- Select an unknown parent component without evidence.
- Treat an unapproved document as an authoritative policy.

When no applicable approved instruction is retrieved,
the assistant must say that sufficient approved guidance
was not found and recommend human review.
