# SHL Assessment Recommendation Agent

Conversational retrieval for the SHL Assessment Catalog.

---

A FastAPI service that recommends SHL assessments through multi-turn conversations. The system maintains conversational context, clarifies ambiguous hiring requirements, retrieves relevant assessments from the SHL catalog, and returns structured recommendations.

## Core Capabilities

- Clarifies incomplete hiring requests
- Recommends relevant SHL assessments
- Supports recommendation refinement
- Compares assessments
- Rejects prompt injection and off-topic requests
- Uses only the SHL catalog as its knowledge source

## Technical Approach

The recommendation pipeline follows a retrieval-first architecture.

```
Conversation
      │
      ▼
Intent Extraction
      │
      ▼
Conversation State
      │
      ▼
Business Rules
      │
      ▼
Hybrid Retrieval
(BM25 + RapidFuzz)
      │
      ▼
Ranked Recommendations
```

No external LLM is used for retrieval decisions. Recommendations are generated deterministically from the indexed SHL catalog.

## API

### Health Check

```
GET /health
```

### Recommendation

```
POST /chat
```

The API is fully stateless. Every request contains the complete conversation history.

## Running

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Deployment

API

https://shl-assessment-recommender-2wy2.onrender.com

Documentation

https://shl-assessment-recommender-2wy2.onrender.com/docs

## Repository Structure

```
app/
data/
scripts/
tests/
```

---

Built by Ayush Agarwal
