---
slug: malayalam-news-digest
title: A language workflow from feed to inbox.
summary: A local prototype combining news ingestion, language-model processing and
  delivery.
category: software
kind: Local application prototype
period: Earlier portfolio work
role: Python workflow integration
tools:
- Python
- OpenAI API
- SQLite
- Gmail API
order: 100
image: assets/images/digest.svg
image_alt: A language workflow from feed to inbox. — explanatory diagram
image_caption: Explanatory schematic created for this portfolio; not a photograph,
  application screenshot or measured output.
featured: false
draft: false
sources:
- label: Source basis
  note: Earlier supplied local code archive and CV project descriptions. No public
    repository is linked.
---

## The problem
Following Malayalam news in English involves collecting articles, translating or summarising them, and packaging the results into a readable digest. This prototype connects those steps in a single Python workflow.

## My contribution
I developed modules for RSS ingestion, Malayalam-to-English translation and summarisation, SQLite article storage, HTML digest generation and Gmail API integration.

## Technical approach
The workflow ingests article metadata and uses stored identifiers to avoid repeated records. A language model produces English text, which is assembled into an HTML digest. Gmail integration uses local OAuth configuration rather than embedded credentials.

## Results & evidence
The earlier local implementation contains the ingestion, storage, processing and delivery components. This case study is based on the supplied project code and CV material. It is **not currently presented as a public, reproducible repository or a deployed daily service**.

## Limitations
Delivery-state ordering, source configuration and date-field consistency require cleanup before the workflow can be described as dependable. Translation and summarisation quality have not been systematically measured.

No private news output, subscriber address, OAuth token or API key is published. The workflow diagram is illustrative and is not an actual delivered email.
