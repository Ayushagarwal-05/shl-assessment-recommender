# SHL Assessment Recommendation Agent

> Conversational recommendation system built for the SHL AI Intern Take-Home Assignment.

A conversational recommendation agent that helps recruiters and hiring teams identify the most relevant SHL assessments based on hiring requirements, job roles, skills, seniority, and business context.

---

## Live Demo

| Service | URL |
|----------|-----|
| API | https://shl-assessment-recommender-2wy2.onrender.com |
| Swagger UI | https://shl-assessment-recommender-2wy2.onrender.com/docs |

---

# Features

- Conversational assessment recommendations
- Context-aware multi-turn conversations
- Automatic clarification for incomplete hiring requests
- Hybrid retrieval using BM25 + RapidFuzz
- Recommendation refinement across conversation turns
- Assessment comparison support
- Unsupported skill detection
- Off-topic request handling
- Prompt injection resistance
- FastAPI REST API

---

# Architecture

```
                User Conversation
                       │
                       ▼
                 FastAPI Endpoint
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
       Hybrid Retrieval (BM25 + RapidFuzz)
                       │
                       ▼
          Ranked SHL Recommendations
                       │
                       ▼
               Structured JSON Response
```

---

# Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- BM25 (`rank-bm25`)
- RapidFuzz

---

# Project Structure

```text
.
├── app/
│   ├── agent.py
│   ├── catalog.py
│   ├── comparison.py
│   ├── intent.py
│   ├── main.py
│   ├── models.py
│   ├── retrieval.py
│   ├── rules.py
│   └── state.py
│
├── data/
│   ├── catalog.json
│   └── conversations/
│
├── scripts/
├── tests/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Ayushagarwal-05/shl-assessment-recommender

cd shl-assessment-recommender
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check endpoint |
| POST | `/chat` | Conversational recommendation endpoint |

---

## Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need Java assessments for hiring developers."
    }
  ]
}
```

---

## Example Response

```json
{
  "reply": "Based on your requirements, I recommend the following SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "...",
      "test_type": "Knowledge & Skills"
    }
  ],
  "end_of_conversation": false
}
```

---

# Recommendation Pipeline

1. Parse conversation history
2. Extract user intent
3. Maintain conversation state
4. Apply business rules
5. Retrieve relevant SHL assessments
6. Rank recommendations
7. Return structured JSON response

---

# Supported Behaviors

- Multi-turn conversations
- Clarification questions
- Recommendation refinement
- Assessment comparison
- Unsupported technology handling
- Off-topic request handling
- Prompt injection resistance

---

# Design Decisions

- Uses deterministic retrieval rather than an LLM to produce consistent recommendations.
- Maintains conversational context through the complete message history supplied in each request.
- Combines BM25 lexical search with RapidFuzz similarity scoring for hybrid retrieval.
- Returns structured JSON responses aligned with the assignment schema.

---

# Known Limitations

- Recommendation quality depends on the available SHL catalog metadata.
- Assessment comparison is based on catalog information rather than semantic reasoning.
- The system currently uses deterministic retrieval and does not incorporate external LLMs.

---

# Deployment

Hosted on **Render**.

| Service | URL |
|----------|-----|
| API | https://shl-assessment-recommender-2wy2.onrender.com |
| Swagger UI | https://shl-assessment-recommender-2wy2.onrender.com/docs |

---

Built by **Ayush Agarwal**

- GitHub: https://github.com/Ayushagarwal-05
- LinkedIn: https://www.linkedin.com/in/ayush-agarwal-39303728b/
