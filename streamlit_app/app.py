# app.py
import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import os

# Cached DB reader
@st.cache_data
def get_data():
    dbname = os.getenv("DB_NAME", "crypto")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "yourpass")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    df = pd.read_sql("SELECT * FROM crypto_history", conn)
    conn.close()
    return df

st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("📈 Cryptocurrency Trends Dashboard")

df = get_data()

# Sidebar filters
coin = st.sidebar.selectbox("Select Coin", sorted(df["name"].unique()))
metric = st.sidebar.selectbox("Metric", ["current_price", "market_cap", "total_volume"])

# Filter data
coin_df = df[df["name"] == coin].sort_values("date")

# Show current stats
latest = coin_df.iloc[-1]
st.subheader(f"{coin} - Latest Snapshot ({latest['date']})")
st.metric("Price (USD)", f"${latest['current_price']:.2f}")
st.metric("Market Cap", f"${latest['market_cap']:,}")
st.metric("24h Volume", f"${latest['total_volume']:,}")

# Historical Line Chart
st.subheader(f"{coin} - {metric.replace('_', ' ').title()} Over Time")
fig = px.line(coin_df, x="date", y=metric, title=f"{coin} {metric} trend")
st.plotly_chart(fig, use_container_width=True)

# Optional: Top 10 table
st.subheader("Top 10 Coins by Market Cap (Latest Date)")
latest_date = df["date"].max()
top_10 = df[df["date"] == latest_date].sort_values("market_cap", ascending=False).head(10)
st.dataframe(top_10[["name", "current_price", "market_cap", "total_volume"]])