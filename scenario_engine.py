def generate_scenario(asset, stride, interface, ecu):

    if stride == "Spoofing":
        return f"Attacker sends spoofed {interface} messages to manipulate {asset} in {ecu} ECU."

    elif stride == "Tampering":
        return f"Attacker modifies {asset} through compromised {interface} communication affecting {ecu} ECU."

    elif stride == "Denial of Service":
        return f"Attacker floods the {interface} network causing disruption of {asset} in {ecu} ECU."

    elif stride == "Information Disclosure":
        return f"Sensitive information from {asset} in {ecu} ECU is exposed through {interface} communication."

    elif stride == "Elevation of Privilege":
        return f"Attacker gains unauthorized privileges allowing manipulation of {asset} in {ecu} ECU."

    else:
        return f"Attack affecting {asset} through {interface} interface in {ecu} ECU."