def generate_stride_threats(asset_name, property, interface):

    threats = []

    if property == "Integrity":

        threats.append({
            "stride": "Tampering",
            "description": f"Unauthorized modification of {asset_name}",
            "attack_path": f"{interface} interface exploitation",
            "impact": 3
        })

        threats.append({
            "stride": "Spoofing",
            "description": f"Impersonation attack affecting {asset_name}",
            "attack_path": f"{interface} message injection",
            "impact": 3
        })

    if property == "Confidentiality":

        threats.append({
            "stride": "Information Disclosure",
            "description": f"Unauthorized access to {asset_name}",
            "attack_path": f"{interface} data interception",
            "impact": 3
        })

    if property == "Availability":

        threats.append({
            "stride": "Denial of Service",
            "description": f"Disruption of {asset_name}",
            "attack_path": f"{interface} flooding attack",
            "impact": 2
        })

    return threats