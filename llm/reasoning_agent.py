from llm.ollama_client import call_ollama
from llm.prompts import medical_explanation_prompt

def generate_explanation(features, symptoms, risk_level):
    prompt = medical_explanation_prompt(features, symptoms, risk_level)
    return call_ollama(prompt)

