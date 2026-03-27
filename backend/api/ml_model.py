import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = None
model = None

def bert_analysis(text):
    return {
        "entities": ["fever", "cough"],
        "severity": "moderate"
    }

def rag_pipeline(symptoms):
    knowledge_base = {
        "fever": "Fever is often caused by infection.",
        "cough": "Cough is related to respiratory infections.",
        "headache": "Headache can be due to stress or migraine.",
        "vomiting": "Vomiting may indicate food poisoning."
    }

    context = []
    for word in symptoms.lower().split():
        if word in knowledge_base:
            context.append(knowledge_base[word])

    return " ".join(context) if context else "General medical condition."


def llm_generate(diagnosis):
    return f"Based on symptoms, patient may have {diagnosis}. Suggested treatment: Rest, hydration, consult doctor."

def train_model():
    global vectorizer, model

    data = {
        "symptoms": [
            "fever", "high fever", "cough", "dry cough",
            "chest pain", "vomiting", "headache", "cold"
        ],
        "diagnosis": [
            "viral infection", "viral infection", "respiratory infection", "respiratory infection",
            "cardiac issue", "food poisoning", "migraine", "common cold"
        ]
    }

    df = pd.DataFrame(data)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["symptoms"])

    model = LogisticRegression()
    model.fit(X, df["diagnosis"])


def predict_disease(symptom_text):
    global vectorizer, model

    if model is None:
        train_model()

    input_data = vectorizer.transform([symptom_text])
    prediction = model.predict(input_data)[0]
    context = rag_pipeline(symptom_text)
    return {
        "diagnosis": prediction,
        "context": context
    }