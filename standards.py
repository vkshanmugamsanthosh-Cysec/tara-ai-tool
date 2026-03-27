# Impact rating definitions
IMPACT_SCALE = {
    0: "No impact",
    1: "Low impact",
    2: "Moderate impact",
    3: "Severe impact"
}

# Attack feasibility definitions
FEASIBILITY_SCALE = {
    1: "Low",
    2: "Medium",
    3: "High"
}

# Risk level logic
def get_risk_level(risk):
    if risk >= 12:
        return "High"
    elif risk >= 6:
        return "Medium"
    else:
        return "Low"