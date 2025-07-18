# transform.py
import pandas as pd

def transform(data):
    df = pd.DataFrame(data)
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume", "last_updated"]]
    df["last_updated"] = pd.to_datetime(df["last_updated"])
    return df
