---
slug: movie-recommender
title: Explaining movie recommendations.
summary: A content-based recommender that makes the ingredients of similarity visible.
category: software
kind: Personal project
period: Current portfolio
role: Python application & recommendation logic
tools:
- Python
- scikit-learn
- pandas
- Streamlit
order: 10
image: assets/images/movie.svg
image_alt: Explaining movie recommendations. — explanatory diagram
image_caption: Explanatory schematic created for this portfolio; not a photograph,
  application screenshot or measured output.
featured: true
draft: false
sources:
- label: README, data audit and implementation
  url: https://github.com/aravindsudheer01-arch/movie-recommendation-system
- label: Weighted scoring implementation
  url: https://github.com/aravindsudheer01-arch/movie-recommendation-system/blob/main/recommender2.py
repository: https://github.com/aravindsudheer01-arch/movie-recommendation-system
---

## The problem
A list of recommendations is more useful when a user can understand why an item was suggested. This project explores movie similarity using catalogue metadata rather than a user's viewing history.

## My contribution
I developed a Python recommendation application with a Streamlit interface, a combined-text TF-IDF baseline, and a weighted alternative. Data preparation, recommendation logic and the interface are separated into modules.

The application supports title search, duplicate-title disambiguation and feature-level similarity explanations. A preparation script combines the original movie and credits files; validation checks required columns and duplicate identifiers.

## Technical approach
The baseline joins genres, keywords and plot text in a single TF-IDF representation. The weighted model creates a separate representation for genres, keywords, overview, director and cast, then combines their cosine similarities.

The default weights are **25%, 25%, 25%, 10% and 15%**, respectively. These are hand-selected design choices, not learned coefficients. The weights are renormalised across usable features for the selected movie, and zero-similarity results are excluded.

## Results & evidence
The public repository includes both implementations, a data-preparation script, a catalogue inspection utility and synthetic tests. The README documents a locally used **4,803-record** dataset. That original processed file is not redistributed in the repository.

The interface can show one to ten recommendations and a feature-score breakdown. The diagram above explains the scoring workflow; it is not a screenshot of a live run.

## Limitations
There is no ratings-based personalisation, collaborative filtering or measured user-relevance evaluation. A similarity score is not a probability that someone will enjoy a film. The weighted approach has not been shown to outperform the baseline.

Flattened cast strings can lose multiword actor identities. Regenerating the data from structured source files is preferable for cast-aware comparisons. Source-data access and redistribution terms must be checked separately.
