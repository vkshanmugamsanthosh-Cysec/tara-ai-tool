import json

def load_threats(interface):

    with open("threat_library.json") as file:
        threats = json.load(file)

    if interface in threats:
        return threats[interface]

    return []