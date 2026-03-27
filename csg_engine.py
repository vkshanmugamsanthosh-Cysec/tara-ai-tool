def generate_csg(asset, stride, ecu):

    if stride == "Spoofing":
        return f"Prevent unauthorized impersonation affecting {asset} in {ecu} ECU."

    elif stride == "Tampering":
        return f"Ensure integrity of {asset} in {ecu} ECU."

    elif stride == "Denial of Service":
        return f"Ensure availability of {asset} in {ecu} ECU."

    elif stride == "Information Disclosure":
        return f"Protect confidentiality of {asset} in {ecu} ECU."

    elif stride == "Elevation of Privilege":
        return f"Prevent unauthorized privilege escalation affecting {asset} in {ecu} ECU."

    else:
        return f"Protect {asset} in {ecu} ECU from cybersecurity threats."