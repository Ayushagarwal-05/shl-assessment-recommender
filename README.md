<div align="center">

# SHL Assessment Recommendation Agent

Conversational Retrieval System for SHL Assessments

<br>

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)

</div>

---

## Overview

The SHL Assessment Recommendation Agent is a conversational recommendation system built for recruiters and hiring managers. It identifies suitable SHL assessments through dialogue instead of traditional keyword search.

---

## Highlights

- Multi-turn conversations
- Clarification questions
- Recommendation refinement
- Assessment comparison
- BM25 retrieval
- RapidFuzz ranking
- FastAPI backend

---

## Architecture

```
User
 │
 ▼
FastAPI
 │
 ▼
Conversation State
 │
 ▼
Intent Extraction
 │
 ▼
Rule Engine
 │
 ▼
Retriever
 │
 ▼
Recommendation
```

---

## API

| Method | Endpoint |
|---------|----------|
| GET | `/health` |
| POST | `/chat` |

---

## Example

```json
{
  "messages":[
    {
      "role":"user",
      "content":"Hiring a Java Developer"
    }
  ]
}
```

---

## Deployment

https://shl-assessment-recommender-2wy2.onrender.com

---

Made by Ayush Agarwal
