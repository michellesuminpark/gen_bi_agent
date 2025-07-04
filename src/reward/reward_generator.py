print("✅ reward_generator.py loaded")


class RewardGenerator:
    def __init__(self, weights=None):
        self.weights = weights or {
            "faithfulness": 0.5,
            "attribution": 0.3,
            "coherence": 0.2
        }

    def compute_reward(self, scores: dict) -> float:
        return sum(self.weights[k] * scores[k] for k in scores)
