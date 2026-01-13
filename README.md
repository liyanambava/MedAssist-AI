# 🏥 MedAssist AI

**Multi-Modal Medical Decision Support System (CV + LLM)**

> ⚠️ **Disclaimer**: This project is an AI-assisted medical **decision-support tool**, not a diagnostic system. It does **not** replace professional medical advice.

---

## 📌 Overview

**MedAssist AI** is a privacy-preserving, offline **AI decision-support system** that helps users interpret medical images (e.g., rashes, wounds, scans) along with basic symptom information to receive **explainable guidance and risk assessment**.

Unlike symptom-search engines, this system focuses on:

* Explainability
* Risk triage
* Ethical AI boundaries

It intentionally avoids diagnosis and prescription.

---

## 🎯 Key Objectives

* Provide calm, structured medical guidance
* Reduce misinformation from generic internet searches
* Combine **computer vision + medical language models**
* Maintain ethical and safety constraints

---

## 🧠 System Capabilities

### User Inputs

* 📸 Medical image (rash, wound, scan, etc.)
* 📝 Structured symptom inputs (pain, fever, duration)
* ✍️ Optional free-text notes

### Outputs

* 🔍 Visual feature analysis (redness, irregularity, brightness)
* 🧠 Human-readable medical explanation
* ⚠️ Risk classification:

  * 🟢 Low
  * 🟡 Medium
  * 🔴 High
* 📌 Clear next-step guidance
* 🚫 Explicit non-diagnostic disclaimer

---

## 🧩 Architecture Overview

```
User
 │
 │  (Image + Symptoms)
 ▼
Streamlit UI
 │
 ▼
Input Validation & Safety Guard
 │
 ├──▶ Vision Feature Extraction (CV)
 │         ├─ Redness
 │         ├─ Brightness
 │         └─ Irregularity
 │
 ├──▶ LLM Reasoning Engine (Local)
 │         ├─ Medical explanation
 │         ├─ Uncertainty handling
 │         └─ Safe language generation
 │
 └──▶ Risk & Triage Engine
           ├─ Rule-based severity assessment
           └─ Action-oriented guidance
```

---

## 🧠 Design Philosophy

### 1️⃣ Not Diagnosis — Decision Support

The system **never names diseases**. It focuses on:

* Possible explanations
* Risk severity
* When to consult a professional

### 2️⃣ Explainable AI

Instead of black-box predictions:

* Visual features are explicit
* Risk logic is rule-based
* Reasoning is transparent

### 3️⃣ Privacy-First

* Uses **local LLMs**
* No cloud APIs
* No medical data storage

### 4️⃣ Safety by Design

* Hard refusal for diagnosis requests
* No emergency override
* No medication advice

---

## 🔧 Technology Stack

### Computer Vision

* OpenCV
* Feature-based analysis (no disease classification)

### Language Model

* Local medical-tuned LLM (via Ollama)
* Medical explanation & reasoning only

### Backend Logic

* Rule-based risk assessment
* Explicit safety guardrails

### Frontend

* Streamlit (clean, minimal UI)

---

## 🗂️ Project Structure (MVP)

```
medassist-ai/
│
├── app/
│   └── main.py
│
├── vision/
│   └── features.py
│
├── llm/
│   ├── ollama_client.py
│   ├── prompts.py
│   └── reasoning_agent.py
│
├── triage/
│   ├── rules.py
│   └── risk_assessment.py
│
├── safety/
│   └── guardrails.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Install and start Ollama

* Download from [https://ollama.com](https://ollama.com)
* Pull a medical-tuned model:

```bash
ollama pull medllama2
```

### 3️⃣ Run the app

```bash
streamlit run app/main.py
```

---

## ⚠️ Ethical Disclaimer

This system:

* ❌ Does NOT diagnose medical conditions
* ❌ Does NOT provide treatment or prescriptions
* ❌ Does NOT replace medical professionals

It is intended for:

* Educational purposes
* Preliminary guidance
* Risk awareness

---

## 📈 Future Improvements

* Grad-CAM visual explainability
* Vision-language multimodal models
* Medical dataset benchmarking
* Symptom NLP parsing
* Confidence calibration

---

## 🧠 Why This Project Matters

This project demonstrates:

* Applied AI system design
* Multi-modal reasoning
* Ethical AI implementation
* Real-world problem framing

It prioritizes **responsibility over hype**.
