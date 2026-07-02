# SHL Assessment Recommendation Agent

> A conversational retrieval system that recommends relevant SHL assessments through natural language interaction.

---

### Built With

FastAPI · Python · BM25 · RapidFuzz

---

## Overview

This project implements a conversational recommendation agent for the SHL Product Catalog.

Instead of relying on keyword search alone, the system understands hiring intent through dialogue, asks clarification questions when required, retrieves relevant assessments, and returns structured recommendations through a stateless FastAPI API.

---

## Features

- Conversational assessment recommendations
- Clarification for vague hiring requests
- Recommendation refinement
- Assessment comparison
- Hybrid retrieval (BM25 + Fuzzy Matching)
- Prompt injection resistance
- Off-topic request handling

---

## API

| Endpoint | Description |
|----------|-------------|
| `GET /health` | Health Check |
| `POST /chat` | Conversational Recommendation API |

---

## Running Locally

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Deployment

Live API

https://shl-assessment-recommender-2wy2.onrender.com

Swagger

https://shl-assessment-recommender-2wy2.onrender.com/docs

---

## Project Structure

```text
app/
data/
scripts/
tests/
```

---

Developed by Ayush Agarwal
