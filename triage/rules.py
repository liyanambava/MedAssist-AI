def assess_risk(features, symptoms):
    redness = features["redness"]
    irregularity = features["irregularity"]
    pain = symptoms["pain"]
    fever = symptoms["fever"]
    duration = symptoms["duration_days"]

    # High risk rules
    if fever and pain >= 7:
        return "HIGH"
    if irregularity > 0.15 and duration > 7:
        return "HIGH"

    # Medium risk rules
    if redness > 20 or pain >= 4:
        return "MEDIUM"
    if duration > 3:
        return "MEDIUM"

    # Low risk
    return "LOW"
