def infer_specialty(features, symptoms):
    notes = symptoms.get("notes", "").lower()

    # --- Dermatology / Skin ---
    if any(word in notes for word in [
        "skin", "rash", "itch", "itching", "lesion", "redness",
        "acne", "eczema", "psoriasis", "hives", "blister",
        "dermatitis", "allergy", "irritation", "irritant",
        "soap", "detergent", "chemical", "cosmetic",
        "burning skin", "dry skin", "scaly", "peeling"
    ]):
        return "Dermatology"

    # --- ENT ---
    if any(word in notes for word in [
        "ear", "ear pain", "throat", "sore throat", "nose",
        "sinus", "tonsil", "hearing", "voice", "nasal",
        "runny nose", "blocked nose", "cold", "cough"
    ]):
        return "ENT"

    # --- Cardiology ---
    if any(word in notes for word in [
        "chest", "chest pain", "heart", "palpitations",
        "heartbeat", "shortness of breath", "breathless",
        "bp", "blood pressure", "pressure in chest"
    ]):
        return "Cardiology"

    # --- Orthopedics ---
    if any(word in notes for word in [
        "joint", "bone", "fracture", "sprain", "knee",
        "back pain", "shoulder", "ankle", "muscle pain",
        "stiffness", "swelling joint", "movement pain"
    ]):
        return "Orthopedics"

    # --- Neurology ---
    if any(word in notes for word in [
        "headache", "migraine", "dizziness", "vertigo",
        "seizure", "numbness", "tingling",
        "memory", "confusion", "fainting"
    ]):
        return "Neurology"

    # --- Gastroenterology ---
    if any(word in notes for word in [
        "stomach", "abdomen", "abdominal pain", "digestion",
        "acid reflux", "heartburn", "vomiting",
        "nausea", "diarrhea", "constipation", "bloating"
    ]):
        return "Gastroenterology"

    # --- Gynecology ---
    if any(word in notes for word in [
        "period", "menstrual", "missed period", "pregnancy",
        "pelvic pain", "pcos", "ovary", "uterus",
        "irregular periods"
    ]):
        return "Gynecology"

    # --- Urology ---
    if any(word in notes for word in [
        "urine", "urination", "bladder", "kidney",
        "burning urine", "frequent urination",
        "pain while urinating"
    ]):
        return "Urology"

    # --- Ophthalmology ---
    if any(word in notes for word in [
        "eye", "vision", "blurred vision", "red eye",
        "watering", "itchy eyes", "eye pain",
        "light sensitivity"
    ]):
        return "Ophthalmology"

    # --- General Medicine (fallback) ---
    return "General Medicine"
