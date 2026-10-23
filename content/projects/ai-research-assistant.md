---
slug: ai-research-assistant
title: A research assistant with traceable sources.
summary: Tool-calling, structured responses and source provenance in a small Python
  CLI.
category: software
kind: Personal prototype
period: Current portfolio
role: LLM integration & application workflow
tools:
- Python
- LangChain
- OpenAI API
- Pydantic
order: 20
image: assets/images/agent.svg
image_alt: A research assistant with traceable sources. — explanatory diagram
image_caption: Explanatory schematic created for this portfolio; not a photograph,
  application screenshot or measured output.
featured: true
draft: false
sources:
- label: Repository and documented limitations
  url: https://github.com/aravindsudheer01-arch/ai-research-agent
- label: CLI and structured response flow
  url: https://github.com/aravindsudheer01-arch/ai-research-agent/blob/main/main.py
repository: https://github.com/aravindsudheer01-arch/ai-research-agent
---

## The problem
A generated answer can look convincing even when its source list is unreliable. This prototype explores how a small research workflow can expose the sources returned by a search tool and save a consistently structured report.

## My contribution
I integrated web search, an OpenAI model, a Pydantic response schema and timestamped file storage in a Python command-line application. The application separates the agent entry point, search, evidence reconciliation and persistence.

## Technical approach
A question enters a LangChain agent with a DDGS search tool. The requested response contains a topic, summary, source URLs and tool usage. The application checks proposed URLs against links actually observed in search responses, then saves the reconciled report.

Saving is deterministic application logic after a structured response, rather than a separate autonomous agent action. Model choice is configurable through local environment settings. Credentials and generated personal reports are excluded from version control.

## Results & evidence
The repository includes the CLI, configuration example, source-filtering helper and tests for report reconciliation and storage. It handles blank input, missing API credentials and runtime failures. Live end-to-end execution still needs network access, API quota and working dependencies.

The visual above is a workflow diagram, not an example generated answer or evidence that a live run succeeded.

## Limitations
Search returns links and snippets; this prototype does not independently read complete documents or verify each claim. A URL appearing in a search result does not prove it supports a statement.

Search failure or empty evidence needs explicit handling before relying on a report. Offline helper tests are not an evaluation of research quality. This is not RAG over a document collection, a trained language model or an academic research engine.
