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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 phase2.py signals.json")
        sys.exit(1)

    signals = load_signals(sys.argv[1])

    insights = reason_about_app(signals)
    ai = ai_reason(signals)

    print("=== Phase 2: Reasoned Analysis ===")
    print("Package:", signals["app_meta"]["package"])

    print("\nRule-Based Insights:")
    for i, line in enumerate(insights, 1):
        print(f"{i}. {line}")

    print("\nAI Summary:")
    print(ai["summary"])

    print("\nAI Key Behaviors:")
    for b in ai["key_behaviors"]:
        print("-", b)

    print("\nAI Suggested Focus Areas:")
    for f in ai["focus_areas"]:
        print("-", f)

    print("\nLimitations:")
    print("-", ai["limitations"])

if __name__ == "__main__":
    main()
