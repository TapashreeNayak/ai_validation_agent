# FRC Component Hierarchy Rules

Document ID: FRC-HIER-001
Version: 1.0
Status: DEMO_APPROVED
Owner: Reference Data Governance

## Parent component validation

1. A parent component code, when provided, must refer
   to an existing component in the applicable dataset.
2. A component cannot be its own parent.
3. Do not infer a parent from a component name alone.
4. When a parent reference cannot be resolved, request
   confirmation from the authorized data owner.
5. Before changing a parent relationship, review the
   approved hierarchy and applicable ownership rules.

## Evidence requirements

For every suggested hierarchy correction, record:

- The affected component code.
- The current parent component code.
- The applicable hierarchy rule.
- The supporting approved document.
- Whether the suggested correction is confirmed or
  requires data-owner review.
