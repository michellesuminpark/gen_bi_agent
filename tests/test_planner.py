from src.planner.planner import Planner

### English ver.

def test_help_query():
    planner = Planner()
    modules = planner.decide("Can you clarify this result?")
    assert modules == ["rewriter", "retriever", "generator", "verifier"]

def test_trend_query():
    modules = Planner().decide("Show me the recent trend in this data.")
    assert modules == ["retriever", "generator", "verifier"]

def test_total_count_query():
    modules = Planner().decide("What is the total number of people who moved?")
    assert modules == ["retriever", "generator", "verifier"]

def test_avg_distribution_query():
    modules = Planner().decide("Can you tell me the average income?")
    assert modules == ["retriever", "generator", "verifier"]

def test_summary_query():
    modules = Planner().decide("Can you give me a general overview of the dataset?")
    assert modules == ["retriever", "generator"]

def test_unknown_query():
    modules = Planner().decide("What’s going on in this spreadsheet?")
    assert modules == ["retriever", "generator", "verifier"]  # fallback


### Korean ver.

def test_korean_trend_query():
    planner = Planner()
    modules = planner.decide("이 데이터의 추세를 보여줘")
    assert modules == ["retriever", "generator", "verifier"]

def test_korean_total_query():
    planner = Planner()
    modules = planner.decide("서울로 이사 온 사람 수는 몇 명인가요?")
    assert modules == ["retriever", "generator", "verifier"]

def test_korean_avg_query():
    planner = Planner()
    modules = planner.decide("평균 연령을 알려줘")
    assert modules == ["retriever", "generator", "verifier"]
