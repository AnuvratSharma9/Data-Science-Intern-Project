import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

st.title("Trader Dashboard")

# load data
df = pd.read_csv("daily_metrics.csv")

# -----------------------------
# Sidebar filter
# -----------------------------
st.sidebar.header("Filter")

sentiment = st.sidebar.selectbox(
    "Select Sentiment",
    df["classification"].unique()
)

df_filtered = df[df["classification"] == sentiment]

# -----------------------------
# KPIs (top row)
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(df_filtered["Closed PnL"].mean(), 2))
col2.metric("Win Rate", round(df_filtered["win"].mean(), 2))
col3.metric("Avg Trades", round(df_filtered["trade_count"].mean(), 2))

# -----------------------------
# Side-by-side charts
# -----------------------------
col4, col5 = st.columns(2)

# Performance
with col4:
    st.subheader("Performance")
    performance = df.groupby("classification")[["Closed PnL","win"]].mean()
    
    st.bar_chart(performance)

# Behavior
with col5:
    st.subheader("Behavior")
    behavior = df.groupby("classification")[["trade_count","avg_size","long_ratio"]].mean()
    
    st.bar_chart(behavior)

st.subheader("Profitability by Cluster")

cluster_perf = df_filtered.groupby("cluster")["Closed PnL"].mean()

st.bar_chart(cluster_perf)