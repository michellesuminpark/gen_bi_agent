

from difflib import SequenceMatcher 
# SequenceMatcher is character-level string similarity. 
# Will probably work with better alternatives

class Verifier:
    def evaluate(self, claim: str, evidence: str) -> dict:
        similarity = SequenceMatcher(None, claim, evidence).ratio()
        return {
            "faithfulness": round(similarity, 2),
            "attribution": round(similarity * 0.95, 2),
            "coherence": round(similarity * 0.9, 2)
        }

print("✅ verifier.py upgraded")
