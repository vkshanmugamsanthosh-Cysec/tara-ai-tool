def get_impact_by_asset(asset_type):
    mapping = {
        "Function": (3, 2, 3, 1),
        "Software": (2, 2, 2, 1),
        "Communication": (2, 1, 2, 1),
        "Credential": (1, 3, 1, 3),
        "Data": (1, 2, 1, 3)
    }
    return mapping.get(asset_type, (1, 1, 1, 1))


def get_feasibility_by_interface(interface):
    mapping = {
        "CAN": (2, 2, 2, 2),
        "OTA": (3, 3, 2, 3),
        "Bluetooth": (2, 2, 2, 1)
    }
    return mapping.get(interface, (1, 1, 1, 1))


def compute_risk(asset_type, interface):
    s, f, o, p = get_impact_by_asset(asset_type)
    impact = max(s, f, o, p)

    e, k, w, eq = get_feasibility_by_interface(interface)
    feasibility = e + k + w + eq

    score = impact * feasibility

    if score >= 20:
        level = "High"
    elif score >= 10:
        level = "Medium"
    else:
        level = "Low"

    return impact, feasibility, score, level