import pandas as pd

def summarize_overall(df: pd.DataFrame) -> dict:
    summary = {
        "total_spend": float(df["spend"].sum()),
        "total_revenue": float(df["revenue"].sum()),
        "overall_roas": float(df["revenue"].sum() / df["spend"].sum()) if df["spend"].sum() > 0 else 0,
        "avg_ctr": float(df["ctr"].mean())
    }
    return summary

def roas_by_date(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    return (
        df.groupby(date_col)
          .agg(spend=("spend", "sum"), revenue=("revenue", "sum"))
          .assign(roas=lambda x: x["revenue"] / x["spend"])
          .reset_index()
    )

def low_ctr_adsets(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    grouped = (
        df.groupby(["campaign_name", "adset_name"])
        .agg(
            impressions=("impressions", "sum"),
            clicks=("clicks", "sum"),
        )
        .reset_index()
    )
    grouped["ctr"] = grouped["clicks"] / grouped["impressions"]
    return grouped[grouped["ctr"] < threshold]
