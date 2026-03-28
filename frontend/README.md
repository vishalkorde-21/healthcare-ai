# 🏥 Healthcare AI Diagnosis System

## 📌 Overview
This project is an AI-powered healthcare system that predicts possible diseases based on patient symptoms and provides treatment suggestions.

It combines:
- Machine Learning (Logistic Regression)
- NLP (BERT-style entity extraction - simulated)
- RAG (Retrieval Augmented Generation - simulated)
- LLM-based treatment suggestion (rule-based)

---

## 🚀 Features
- Predict disease from symptoms
- Extract key entities (fever, cough, etc.)
- Provide medical context (RAG)
- Suggest treatment using AI logic
- REST API using Django
- Swagger UI for testing

---

## 🛠️ Tech Stack
### Backend:
- Python
- Django REST Framework
- Scikit-learn

### Frontend:
- React.js

### Others:
- Swagger (API testing)
- Git & GitHub

---

## ⚙️ How to Run

### Backend:
```bash
cd backend
pip install -r requirements.txt
python manage.py runserver