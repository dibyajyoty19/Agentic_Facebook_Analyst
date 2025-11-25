from typing import List, Dict, Any
import pandas as pd

class CreativeAgent:
    def generate(self, df: pd.DataFrame, low_ctr_threshold: float) -> List[Dict[str, Any]]:
        """
        Generates creative improvements for low CTR campaigns based on existing creative message patterns.
        """

        low_ctr_df = df[df["ctr"] < low_ctr_threshold]

        recommendations = []
        grouped = low_ctr_df.groupby(["campaign_name", "adset_name", "creative_message"])

        for (campaign, adset, message), block in grouped:
            ctr_value = block["ctr"].mean()

            suggestions = {
                "headlines": [
                    "Limited Time Offer — Don’t Miss Out!",
                    "Exclusive Sale Ends Soon!",
                    "Your Favourites Are Almost Gone"
                ],
                "primary_texts": [
                    "You viewed these items recently — now get an extra deal before it's gone!",
                    "Best sellers are selling out fast. Complete your purchase before your size runs out.",
                    "Upgrade your wardrobe with our premium collection — shop before stocks end."
                ],
                "ctas": ["Shop Now", "Claim Offer", "Complete Purchase"]
            }

            recommendations.append({
                "campaign_name": campaign,
                "adset_name": adset,
                "current_message": message,
                "avg_ctr": float(ctr_value),
                "suggestions": suggestions
            })

        return recommendations
