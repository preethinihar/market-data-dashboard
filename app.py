import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Market Dashboard", layout="wide")

st.title("📊 Market Data Analytics Dashboard")

# Stock input
ticker = st.text_input(
    "Enter Stock Symbol (Example: AAPL, TCS.NS, INFY.NS)",
    "AAPL"
)

# Date input
date_range = st.date_input(
    "Select Date Range (optional)",
    value=[]
)

if ticker:

    # Download data
    data = yf.download(
        ticker,
        start=None if not date_range else date_range[0],
        end=None if not date_range else date_range[-1],
    )

    # Handle case when no data
    if data.empty:
        st.warning("No data found. Try another symbol.")
    else:
        # ---- FIX: flatten MultiIndex columns ----
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]

        # Show raw data
        st.subheader("Raw Data")
        st.write(data.tail())

        # Moving averages
        data["MA20"] = data["Close"].rolling(20).mean()
        data["MA50"] = data["Close"].rolling(50).mean()

        # Price chart
        st.subheader("Price Chart with Moving Averages")
        fig = px.line(
            data,
            x=data.index,
            y=["Close", "MA20", "MA50"],
            labels={"value": "Price", "index": "Date"},
        )
        st.plotly_chart(fig, use_container_width=True)

        # Volume chart
        st.subheader("Volume")
        fig2 = px.bar(data, x=data.index, y="Volume")
        st.plotly_chart(fig2, use_container_width=True)

        # Download button
        csv = data.to_csv().encode("utf-8")
        st.download_button(
            "Download Data as CSV",
            csv,
            "market_data.csv",
            "text/csv"
        )
