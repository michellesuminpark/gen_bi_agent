from src.verifier.verifier import Verifier
from src.planner.planner import Planner
from src.reward.reward_generator import RewardGenerator

if __name__ == "__main__":
    v = Verifier()
    r = RewardGenerator()

    score = v.evaluate("The GDP of Korea increased.", "Data shows GDP went up.")
    reward = r.compute_reward(score)

    print("Score:", score)
    print("Reward:", reward)


