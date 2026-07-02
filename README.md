# SHL Assessment Recommendation Agent

> Conversational recommendation system built for the SHL AI Intern Take-Home Assignment.

An intelligent conversational recommendation agent that helps users discover the most relevant SHL assessments based on hiring requirements, job roles, skills, seniority, and business context.

## Live Demo

**API:** https://shl-assessment-recommender-2wy2.onrender.com

**Swagger Docs:** https://shl-assessment-recommender-2wy2.onrender.com/docs

---

## Features

- Conversational recommendation workflow
- Context-aware multi-turn conversations
- Automatic clarification when information is insufficient
- SHL assessment retrieval using BM25 + Fuzzy Matching
- Unsupported skill detection
- Off-topic query handling
- Prompt injection resistance
- Assessment comparison support
- REST API built with FastAPI

---

## Tech Stack

- Python 3.11
- FastAPI
- BM25 (rank-bm25)
- RapidFuzz
- Pydantic

---

## Project Structure

```
.
├── app
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
├── data
│   ├── catalog.json
│   └── conversations/
│
├── scripts
│
├── tests
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Ayushagarwal-05/shl-assessment-recommender.git

cd shl-assessment-recommender
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### Health Check

```
GET /health
```

Example Response

```json
{
  "status": "ok"
}
```

---

### Chat

```
POST /chat
```

Example Request

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

Example Response

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

## Recommendation Pipeline

1. Parse conversation history
2. Extract user intent
3. Maintain conversation state
4. Apply conversational rules
5. Retrieve relevant assessments
6. Rank recommendations
7. Return structured JSON response

---

## Supported Behaviors

- Multi-turn conversations
- Clarification questions
- Refinement requests
- Assessment comparison
- Unsupported technology handling
- Off-topic conversations
- Prompt injection resistance

---

## Deployment

Hosted on Render.

API

https://shl-assessment-recommender-2wy2.onrender.com

Swagger

https://shl-assessment-recommender-2wy2.onrender.com/docs

---

## Author

Ayush Agarwal

GitHub:
https://github.com/Ayushagarwal-05
