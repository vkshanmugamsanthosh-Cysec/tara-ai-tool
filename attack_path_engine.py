def generate_attack_path(interface, ecu):

    if interface == "CAN":
        return f"Attacker → OBD Port → CAN Bus → Gateway ECU → {ecu} ECU"

    elif interface == "OTA":
        return f"Attacker → Internet → OTA Server → Telematics ECU → {ecu} ECU"

    elif interface == "Diagnostics":
        return f"Attacker → OBD Diagnostic Tool → Diagnostic Session → {ecu} ECU"

    else:
        return f"Attacker → External Interface → {ecu} ECU"