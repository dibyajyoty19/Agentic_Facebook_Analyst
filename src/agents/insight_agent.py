from typing import List, Dict, Any

class InsightAgent:
    def generate_hypotheses(self, data_summary: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Creates hypotheses based on observed metric changes such as ROAS and CTR trends.
        """

        hypotheses = []
        roas_ts = data_summary.get("roas_time_series", [])

        # Hypothesis 1 – ROAS trend based reasoning
        if len(roas_ts) >= 2:
            first = roas_ts[0]["roas"]
            last = roas_ts[-1]["roas"]
            change_pct = (last - first) / first if first != 0 else 0

            if change_pct < 0:
                hypotheses.append({
                    "id": "H1",
                    "description": "ROAS has decreased significantly over time. Possible drivers: CTR drop, creative fatigue, or inefficient spend shift.",
                    "expected_pattern": "ROAS down and CTR or purchases also down",
                    "change_pct": round(change_pct, 4)
                })
            else:
                hypotheses.append({
                    "id": "H1",
                    "description": "ROAS increased or remained stable over time.",
                    "expected_pattern": "ROAS stable/up and CTR stable",
                    "change_pct": round(change_pct, 4)
                })

        # Hypothesis 2 – Low CTR impact on ROAS
        if data_summary.get("low_ctr_adsets"):
            hypotheses.append({
                "id": "H2",
                "description": "Some adsets have low CTR which may be negatively affecting ROAS. Possible cause: messaging or audience mismatch.",
                "expected_pattern": "Low CTR adsets show correlated ROAS decline."
            })

        return hypotheses
