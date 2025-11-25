import pandas as pd

def load_dataset(path: str, date_column: str = "date") -> pd.DataFrame:
    df = pd.read_csv(path)
    if date_column in df.columns:
        df[date_column] = pd.to_datetime(df[date_column])
    return df
