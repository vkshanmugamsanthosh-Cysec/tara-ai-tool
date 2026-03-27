import json
import requests
from dotenv import load_dotenv
load_dotenv()
ANTHROPIC_API_KEY = ","  # ← paste your key here

def generate_ai_threats(ecu, interface, assets):

    asset_summary = "\n".join([
        f"- {a['name']} ({a['type']}) — Security Properties: {', '.join(a['security_properties'])}"
        for a in assets
    ])

    prompt = f"""You are an expert Automotive Cybersecurity Engineer with deep knowledge of ISO/SAE 21434, UNECE R155, STRIDE, and HEAVENS threat modeling.

Analyze the following ECU system and generate a detailed TARA (Threat Analysis and Risk Assessment).

ECU: {ecu}
Interface: {interface}

Assets:
{asset_summary}

For each asset, generate realistic threat scenarios using STRIDE methodology.

Respond ONLY in valid JSON format like this (no markdown, no explanation, no extra text):
{{
  "threats": [
    {{
      "asset": "asset name",
      "stride": "STRIDE category",
      "threat_scenario": "detailed realistic threat scenario",
      "attack_path": "step by step attack path",
      "impact": "High/Medium/Low",
      "likelihood": "High/Medium/Low",
      "risk_level": "High/Medium/Low",
      "mitigation": "specific technical mitigation aligned with ISO 21434"
    }}
  ]
}}

Generate at least one threat per asset. Be specific, technical, and realistic for automotive systems."""

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "Content-Type": "application/json",
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01"
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 4000,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=60
        )

        if response.status_code != 200:
            raise Exception(f"API error {response.status_code}: {response.text}")

        data = response.json()
        raw = data["content"][0]["text"].strip()

        # Remove markdown fences if present
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        return json.loads(raw)

    except json.JSONDecodeError as e:
        raise Exception(f"JSON parse error: {str(e)}")
    except Exception as e:
        raise Exception(f"AI engine error: {str(e)}")