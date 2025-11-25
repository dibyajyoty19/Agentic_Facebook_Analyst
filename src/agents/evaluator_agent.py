from typing import List, Dict, Any
import pandas as pd

class EvaluatorAgent:
    def __init__(self, config: dict):
        self.config = config

    def evaluate(self, df: pd.DataFrame, hypotheses: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        evaluated = []

        for h in hypotheses:
            if h["id"] == "H1":
                result = self._evaluate_roas_trend(df, h)
            elif h["id"] == "H2":
                result = self._evaluate_low_ctr(df, h)
            else:
                result = {**h, "is_supported": False, "confidence": 0.2, "evidence": "Not enough rule logic implemented"}

            evaluated.append(result)

        return evaluated

    def _evaluate_roas_trend(self, df: pd.DataFrame, h: Dict[str, Any]) -> Dict[str, Any]:
        # Split dataset into early and late halves
        midpoint = len(df) // 2
        before = df.iloc[:midpoint]
        after = df.iloc[midpoint:]

        before_roas = before["revenue"].sum() / before["spend"].sum()
        after_roas = after["revenue"].sum() / after["spend"].sum()

        drop_pct = (before_roas - after_roas) / before_roas if before_roas > 0 else 0
        threshold = self.config["analysis"]["roas_drop_threshold_pct"]

        is_supported = drop_pct > threshold
        confidence = min(1.0, max(0.0, drop_pct * 2))

        return {
            **h,
            "is_supported": is_supported,
            "confidence": round(confidence, 3),
            "evidence": {
                "before_roas": round(before_roas, 3),
                "after_roas": round(after_roas, 3),
                "drop_pct": round(drop_pct, 3)
            }
        }

    def _evaluate_low_ctr(self, df: pd.DataFrame, h: Dict[str, Any]) -> Dict[str, Any]:
        threshold = self.config["analysis"]["low_ctr_threshold"]
        low_ctr_df = df[df["ctr"] < threshold]

        is_supported = len(low_ctr_df) > 0
        confidence = 0.85 if is_supported else 0.3

        return {
            **h,
            "is_supported": is_supported,
            "confidence": confidence,
            "evidence": {
                "low_ctr_rows": len(low_ctr_df),
                "examples": low_ctr_df[["campaign_name", "adset_name", "ctr"]]
                                .head(3)
                                .to_dict(orient="records")
            }
        }
