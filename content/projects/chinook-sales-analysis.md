---
slug: chinook-sales-analysis
title: Finding the shape of sales.
summary: SQL joins, window functions and business interpretation on a sample retail
  database.
category: data
kind: SQL analysis
period: Current portfolio
role: Query design & analytical interpretation
tools:
- MySQL
- SQL
- CTEs
- Window functions
order: 30
image: assets/images/sql.svg
image_alt: Finding the shape of sales. — explanatory diagram
image_caption: Chart redrawn from the revenue shares reported in the repository. Chinook
  is synthetic sample data; this is not a commercial result.
featured: true
draft: false
sources:
- label: Published queries and findings
  url: https://github.com/aravindsudheer01-arch/chinook-sales-analysis
- label: Revenue shares and window calculations
  url: https://github.com/aravindsudheer01-arch/chinook-sales-analysis/blob/main/03_advanced_queries.sql
repository: https://github.com/aravindsudheer01-arch/chinook-sales-analysis
---

## The problem
Which markets and product categories account for most sales? How does spending vary by customer? This analysis turns related transaction tables into a small set of business-relevant observations.

## My contribution
I wrote SQL queries for billing-country revenue, customer spending, invoice frequency, average invoice value and genre concentration. The queries progress from filtering and grouping to multi-table joins, CTEs, rankings and running totals.

## Technical approach
Customer-level analysis uses the Customer and Invoice tables. Genre revenue is computed from InvoiceLine quantities and unit prices, joined through Track to Genre. This keeps the revenue measure aligned with the question being asked.

CTEs make the genre-revenue calculation reusable. Window functions calculate ranks, total revenue share and cumulative share with an explicit ordering.

## Results & evidence
The repository reports **35.50%** of recorded revenue from Rock and **63.13%** from the top three genres: Rock, Latin and Metal. The first six genres reach **80.93%** of cumulative revenue. These are findings from the sample dataset, not improvements delivered to a business.

| Genre | Revenue share |
| --- | ---: |
| Rock | 35.50% |
| Latin | 16.41% |
| Metal | 11.22% |
| Alternative & Punk | 10.37% |
| TV Shows | 4.02% |
| Jazz | 3.40% |

The chart above redraws the first three values reported in the repository. Percentages are not model performance metrics.

## Limitations
Chinook is a fictional sample store. Billing country is not necessarily a customer's current location. The media catalogue includes non-music categories, and inner joins omit categories without recorded sales.

The findings are descriptive. They do not show that a marketing intervention will cause additional revenue. Invoice-to-line reconciliation and broader data-quality checks are sensible next validation steps, not claimed completed work.
