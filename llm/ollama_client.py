import subprocess

def call_ollama(prompt, model="mistral"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        encoding="utf-8",     
        errors="ignore",
        capture_output=True
    )
    return result.stdout.strip()
