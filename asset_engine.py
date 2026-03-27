import json

def load_assets(ecu):

    with open("asset_library.json") as f:
        assets = json.load(f)

    return assets.get(ecu, [])