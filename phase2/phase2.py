# Phase 2: Hybrid rule-based + AI reasoning layer (stable)
# Phase 2: Hybrid AI + Rule-based reasoning layer

import json
import sys
def load_signals(path):
    with open(path, "r") as f:
        return json.load(f)


def reason_about_app(signals):
    analysis = []

    if len(signals["permissions"]["dangerous"]) == 0:
        analysis.append("No dangerous permissions detected.")

    if len(signals["network"]["urls"]) == 0:
        analysis.append("No explicit network endpoints found.")

    if signals["code_signals"]["reflection"]:
        analysis.append("Uses reflection; dynamic behavior possible.")
    else:
        analysis.append("No reflection usage detected.")

    return analysis

def ai_reason(signals):
    """
    Stub for AI reasoning.
    This will later be replaced with an actual LLM call.
    """
    return {
        "summary": "The application appears to be a legitimate Android app with standard behavior.",
        "key_behaviors": [
            "Uses common Android components",
            "No dangerous permissions observed"
        ],
        "focus_areas": [
            "Core activities handling app updates",
            "Background services if present"
        ],
        "limitations": "AI reasoning is based only on provided static signals."
    }
def get_phase2_output(signals):
    return {
        "rule_based_analysis": reason_about_app(signals),
        "ai_reasoning": ai_reason(signals)
    }
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 phase2.py signals.json")
        sys.exit(1)

    signals = load_signals(sys.argv[1])

    phase2_output = get_phase2_output(signals)

    output = {
        "package": signals["app_meta"]["package"],
        "analysis": phase2_output
    }

    with open("phase2_output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("[+] Phase 2 output written to phase2_output.json")


if __name__ == "__main__":
    main()
