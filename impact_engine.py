def calculate_impact(safety, financial, operational, privacy):

    impact = max(safety, financial, operational, privacy)

    return impact