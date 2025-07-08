# retriever

import pandas as pd

class Retriever:
    """
    Retrieves data slices based on the planner's execution plan.
    For now, supports simple 'intent' types like 'trend', 'sum', 'average', summarize.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def retrieve(self, plan: dict) -> pd.DataFrame:
        intent = plan.get("intent")
        column_hint = plan.get("column_hint")
        filter_hint = plan.get("filter_hint")

        # Intent: trend → return full data (for now)
        if intent == "trend":
            return self.df

        # Intent: sum / total
        elif intent in ["sum", "total"]:
            if column_hint and column_hint in self.df.columns:
                return pd.DataFrame({column_hint: [self.df[column_hint].sum()]})
            else:
                return pd.DataFrame({"error": ["column_hint missing or not found"]})

        # Intent: average
        elif intent == "average":
            if column_hint and column_hint in self.df.columns:
                return pd.DataFrame({column_hint: [self.df[column_hint].mean()]})
            else:
                return pd.DataFrame({"error": ["column_hint missing or not found"]})

        # Intent: summarize
        # temporary sub
        elif intent == "summarize":
            return self.df.head(5)

        # Fallback: return full dataset
        return self.df
