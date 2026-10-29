
# FRC Data Validation Standard

Document ID: FRC-STD-001
Version: 1.0
Status: DEMO_APPROVED
Owner: Reference Data Governance
Effective Date: 2026-01-01

## Rule: DUPLICATE_CODE

Rule ID: FRC-VAL-001

Description:
Each FRC component code must be unique within the
applicable reference dataset.

Failure condition:
The same component code occurs in multiple records.

Required action:
Identify all records with the duplicate code.
Do not automatically delete or rename records.
Refer the conflict to the authorized data owner.

## Rule: MISSING_VALUE

Rule ID: FRC-VAL-002

Description:
Mandatory fields must contain valid values.

Failure condition:
A required field is blank or null.

Required action:
Identify the missing field and record.
Request the valid value from the authorized data owner.
Do not infer missing business values.

## Rule: INVALID_COUNTRY_CODE

Rule ID: FRC-VAL-003

Description:
The country code must comply with the configured
two-letter country-code validation rule.

Failure condition:
The value does not contain exactly two alphabetic letters.

Required action:
Check the approved country reference mapping.
Do not assume that a three-letter code can be
converted automatically to a two-letter code.

## Rule: INVALID_DATE_RANGE

Rule ID: FRC-VAL-004

Description:
The effective end date must not precede the
effective start date.

Failure condition:
Effective end date is earlier than effective start date.

Required action:
Ask the authorized data owner to confirm the
correct effective dates before making changes.

## Rule: INVALID_START_DATE

Rule ID: FRC-VAL-005

Description:
The effective start date must be a valid date
in the accepted input format.

Required action:
Check the source record and request confirmation
if the intended date is unclear.

## Rule: INVALID_STATUS

Rule ID: FRC-VAL-006

Description:
A component status must be included in the
configured approved status list.

Required action:
Look up the approved status mapping.
Do not automatically replace an unsupported
status with another value.

## Rule: UNKNOWN_PARENT

Rule ID: FRC-VAL-007

Description:
A referenced parent component must exist in the
applicable reference dataset when a parent is specified.

Required action:
Check whether the parent code exists.
Request confirmation before adding a new parent
or changing the parent reference.

## Rule: SELF_PARENT

Rule ID: FRC-VAL-008

Description:
A component cannot reference itself as its parent.

Required action:
Review the component hierarchy and obtain the
correct parent reference from the data owner.
