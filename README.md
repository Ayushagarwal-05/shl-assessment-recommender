<div align="center">

# 🎯 SHL Assessment Recommendation Agent

### Conversational AI for Intelligent SHL Assessment Recommendations

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi)]()
[![BM25](https://img.shields.io/badge/Retrieval-BM25-orange)]()
[![RapidFuzz](https://img.shields.io/badge/Fuzzy_Matching-RapidFuzz-success)]()
[![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)]()

**Built for the SHL Generative AI Internship Assignment**

🌐 **Live API:** https://shl-assessment-recommender-2wy2.onrender.com

📖 **Swagger Documentation:** https://shl-assessment-recommender-2wy2.onrender.com/docs

</div>

---

# ✨ Overview

The SHL Assessment Recommendation Agent is a conversational recommendation system that helps recruiters identify the most suitable SHL assessments based on hiring requirements, job roles, experience level, skills, and business context.

Instead of relying on keyword matching alone, the system maintains conversation state, asks clarification questions when needed, retrieves relevant assessments using BM25 + Fuzzy Matching, and returns structured recommendations through a FastAPI REST API.

---

# 🚀 Features

✅ Multi-turn conversational recommendations

✅ Intelligent clarification questions

✅ BM25 + RapidFuzz retrieval pipeline

✅ Conversation state tracking

✅ Unsupported skill detection

✅ Prompt injection resistance

✅ Off-topic query handling

✅ Assessment comparison

✅ REST API with FastAPI

---

# 🏗️ Architecture

```text
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
(BM25 + RapidFuzz)
   │
   ▼
Assessment Ranking
   │
   ▼
JSON Response
```

---

# 📂 Project Structure

```text
app/
│── agent.py
│── catalog.py
│── comparison.py
│── intent.py
│── main.py
│── models.py
│── retrieval.py
│── rules.py
│── state.py

data/
scripts/
tests/
```

---

# ⚙️ Installation

```bash
git clone https://github.com/Ayushagarwal-05/shl-assessment-recommender

cd shl-assessment-recommender

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health Check |
| POST | `/chat` | Conversational Recommendation API |

---

# 💬 Example Request

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

# 📤 Example Response

```json
{
  "reply": "...",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "...",
      "test_type": "Knowledge & Skills"
    }
  ]
}
```

---

# 🧠 Recommendation Pipeline

```text
Conversation
      │
      ▼
Intent Extraction
      │
      ▼
Conversation State
      │
      ▼
Rule Engine
      │
      ▼
Retriever
      │
      ▼
Ranking
      │
      ▼
Recommendations
```

---

# 🌍 Deployment

**Live API**

https://shl-assessment-recommender-2wy2.onrender.com

**Swagger**

https://shl-assessment-recommender-2wy2.onrender.com/docs

---

# 👨‍💻 Author

**Ayush Agarwal**

GitHub: https://github.com/Ayushagarwal-05

LinkedIn: *(add your LinkedIn URL here)*
