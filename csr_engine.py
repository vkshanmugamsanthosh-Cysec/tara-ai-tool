def generate_csr(asset, stride, interface):

    if stride == "Spoofing":

        if interface == "CAN":
            return f"Implement authentication for CAN messages controlling {asset}."

        if interface == "OTA":
            return f"Ensure secure authentication of OTA update commands affecting {asset}."

    elif stride == "Tampering":
        return f"Implement integrity protection mechanisms for {asset}."

    elif stride == "Denial of Service":
        return f"Implement rate limiting and intrusion detection to protect {asset} from DoS attacks."

    elif stride == "Information Disclosure":
        return f"Implement encryption to protect confidentiality of {asset}."

    elif stride == "Elevation of Privilege":
        return f"Implement access control mechanisms to prevent unauthorized privilege escalation affecting {asset}."

    else:
        return f"Implement cybersecurity controls to protect {asset}."