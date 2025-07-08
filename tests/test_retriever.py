import pandas as pd
from src.retriever.retriever import Retriever

# Sample dataset for testing
df = pd.DataFrame({
    "age": [25, 30, 35, 40, 45],
    "district": ["Gangnam", "Jongno", "Mapo", "Jongno", "Gangnam"],
    "purpose": ["민원상담", "정보이용", "견학", "민원상담", "정보이용"]
})


def test_trend_returns_entire_df():
    plan = {"intent": "trend"}
    retriever = Retriever(df)
    result = retriever.retrieve(plan)
    assert result.equals(df)


def test_average_age():
    plan = {"intent": "average", "column_hint": "age"}
    retriever = Retriever(df)
    result = retriever.retrieve(plan)
    expected = pd.DataFrame({"age": [df["age"].mean()]})
    pd.testing.assert_frame_equal(result, expected)


def test_sum_age():
    plan = {"intent": "sum", "column_hint": "age"}
    retriever = Retriever(df)
    result = retriever.retrieve(plan)
    expected = pd.DataFrame({"age": [df["age"].sum()]})
    pd.testing.assert_frame_equal(result, expected)


def test_summarize_returns_preview():
    plan = {"intent": "summarize"}
    retriever = Retriever(df)
    result = retriever.retrieve(plan)
    assert len(result) == 5
    assert all(col in result.columns for col in df.columns)


def test_column_hint_missing_returns_error():
    plan = {"intent": "sum", "column_hint": "nonexistent"}
    retriever = Retriever(df)
    result = retriever.retrieve(plan)
    assert "error" in result.columns
