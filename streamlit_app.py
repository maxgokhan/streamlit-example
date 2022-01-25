import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import yfinance as yf

st.write("""
# Simple Stock Price App
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'BIZIM.IS'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.High)

