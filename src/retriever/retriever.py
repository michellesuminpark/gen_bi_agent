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

        ## Applying the filter first to the df.
        df_filtered = self.df
        if filter_hint:
            try:
                df_filtered = self.df.query(filter_hint)
            except Exception as e:
                return pd.DataFrame({"error": [f"Invalid filter_hint: {e}"]})


        ## Then uses intent
        # Intent: trend → return filtererd data
        if intent == "trend":
            return df_filtered
        
        # Intent: sum / total
        elif intent in ["sum", "total"]:
            if column_hint and column_hint in df_filtered.columns:
                return pd.DataFrame({column_hint: [df_filtered[column_hint].sum()]})
            else:
                return pd.DataFrame({"error": ["column_hint missing or not found"]})

        # Intent: average
        elif intent == "average":
            if column_hint and column_hint in df_filtered.columns:
                return pd.DataFrame({column_hint: [df_filtered[column_hint].mean()]})
            else:
                return pd.DataFrame({"error": ["column_hint missing or not found"]})

        # Intent: summarize
        elif intent == "summarize":
            return df_filtered.head(5)

        # Fallback: return full dataset
        return self.df
