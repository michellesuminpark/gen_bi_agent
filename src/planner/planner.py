class Planner:
    def __init__(self, policy=None):
        self.policy = policy

    def decide(self, query: str, last_reward=None, last_path=None) -> list:
        query = query.lower()

        if any(word in query for word in [
            "help", "clarify", "confusing", "explain better",
            "도움", "모르겠", "설명", "헷갈", "불명확"
        ]):
            return ["rewriter", "retriever", "generator", "verifier"]

        elif any(word in query for word in [
            "trend", "change", "evolution",
            "추세", "변화", "변동", "늘었", "줄었", "증가", "감소"
        ]):
            return ["retriever", "generator", "verifier"]

        elif any(word in query for word in [
            "total", "sum", "count", "how many",
            "총", "전체", "합계", "얼마나", "수", "몇 명"
        ]):
            return ["retriever", "generator", "verifier"]

        elif any(word in query for word in [
            "average", "mean", "distribution",
            "평균", "분포", "중앙값"
        ]):
            return ["retriever", "generator", "verifier"]

        elif any(word in query for word in [
            "overview", "summary", "general", "insight",
            "요약", "개요", "요점", "전체적인", "인사이트"
        ]):
            return ["retriever", "generator"]

        return ["retriever", "generator", "verifier"]
