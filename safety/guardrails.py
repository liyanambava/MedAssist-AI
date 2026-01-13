BANNED_PHRASES = [
    "diagnose",
    "you have",
    "cancer",
    "tumor",
    "prescription",
    "medicine dosage",
    "emergency treatment"
]

def check_safety(user_text):
    text = user_text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in text:
            return False
    return True
