from typing import Dict, Any
import pandas as pd

from src.utils.metrics import summarize_overall, roas_by_date, low_ctr_adsets

class DataAgent:
    def __init__(self, config: dict):
        self.config = config

    def run(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Loads and summarizes key dataset metrics needed for insights.
        """
        date_col = self.config["data"]["date_column"]

        summary = summarize_overall(df)
        roas_ts = roas_by_date(df, date_col=date_col).to_dict(orient="records")

        low_ctr_records = low_ctr_adsets(df, threshold=self.config["analysis"]["low_ctr_threshold"]) \
            .to_dict(orient="records")

        return {
            "summary": summary,
            "roas_time_series": roas_ts,
            "low_ctr_adsets": low_ctr_records
        }
