#Streamlit is an open-source Python library that makes it easy to build and share custom web applications for machine learning and
# data science projects. It allows users to create interactive applications using Python scripts, without needing expertise in front-end
# development. With Streamlit, you can visualize data, display models, and build user-friendly interfaces quickly.

import yfinance as yf
import streamlit as st


st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Apple (AAPL) from 2023 to 2024!

""")


#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-01-01', end='2024-01-01')

st.write("""
# Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
# Volume Price
""")
st.line_chart(tickerDf.Volume)

