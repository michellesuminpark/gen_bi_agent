print("✅ verifier.py loaded")

class Verifier:
    def evaluate(self, claim: str, evidence: str) -> dict:
        return {
            "faithfulness": 0.9,
            "attribution": 0.8,
            "coherence": 0.85
        }
