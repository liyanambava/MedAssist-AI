def get_risk_message(level):
    messages = {
        "LOW": "Low risk based on available information. Monitor symptoms.",
        "MEDIUM": "Moderate risk. Consider consulting a healthcare professional.",
        "HIGH": "Higher risk indicators detected. Seek medical attention."
    }
    return messages[level]
