# Manufacturing Knowledge Base

This directory contains the manufacturing reference documents used by the
Manufacturing AI Copilot retrieval-augmented generation (RAG) workflow.

The documents are intentionally stored outside the application code. This
allows manufacturing knowledge to grow without changing the detector,
analyzer, or API implementation.

## Directory structure

- `pcb_defects/`: defect-specific descriptions, causes, inspection steps, and
  shipment decisions.
- `manufacturing_guides/`: process and test guidance that can apply to more
  than one defect.

## Adding a document

Use clear Markdown headings and keep each file focused on one defect, process,
or inspection procedure. Include concrete inspection and recommended-action
steps where possible. The RAG indexer will later split these documents into
searchable sections while preserving their source file names.

These documents are reference material for AI-generated recommendations. They
should be reviewed by a qualified manufacturing engineer before being used as
an operational standard.
