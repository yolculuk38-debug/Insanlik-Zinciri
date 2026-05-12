# RECORD SCHEMA

## Purpose

This document defines the standard structure used for Humanity Chain interaction records.

The schema is designed to support:

- Transparent archival systems
- Multi-layer verification workflows
- Human-readable records
- Machine-readable validation structures
- Traceable interaction history

---

## Standard Record Fields

Each archived record should contain the following fields:

| Field | Description |
|---|---|
| Record ID | Unique interaction identifier |
| Record Type | Type of archived interaction |
| Model | AI system or participant |
| Date | Record creation date |
| Status | Verification status |
| Prompt | Original input |
| Response | Archived response |
| Hash Reference | SHA-256 integrity reference |
| QR Reference | Verification access layer |
| Timeline Reference | Chronological archive reference |

---

## Verification States

Possible record states:

- Pending
- Verified
- Archived
- Deprecated

---

## Supported Formats

Humanity Chain currently supports:

- Markdown (.md)
- JSON (.json)
- SHA-256 hash references
- QR verification references

---

## Future Extensions

Future schema versions may include:

- Multi-witness verification
- Cross-model validation
- Digital signature layers
- Timestamp verification
- Automated integrity workflows
- Distributed archive synchronization

---

## Version

Current schema version:

```text
record-v1
