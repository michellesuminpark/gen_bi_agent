# generator
import pandas as pd

class Generator:
    def generate(self, df: pd.DataFrame, intent: str, column_hint: str = None) -> str:
        if df.empty:
            return "데이터가 없습니다."

        if intent == "trend" and column_hint:
            values = df[column_hint].tolist()
            if len(values) < 2:
                return f"{column_hint} 컬럼에 데이터가 부족합니다."
            trend = "증가" if values[-1] > values[0] else "감소"
            return f"{column_hint}는 {values[0]:,.0f}에서 {values[-1]:,.0f}로 {trend}했습니다."

        elif intent in ["sum", "total"] and column_hint:
            total = df[column_hint].sum()
            return f"{column_hint}의 총합은 {total:,.2f}입니다."

        elif intent == "average" and column_hint:
            avg = df[column_hint].mean()
            return f"{column_hint}의 평균은 {avg:,.2f}입니다."

        return "요약 정보를 생성할 수 없습니다."

print("✅ generator.py loaded")
