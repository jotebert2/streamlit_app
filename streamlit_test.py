import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.write("""
# # Simple Stock Price App

# Shown are the stock closing price and volume of Google

# 	""")

# tickerSymbol = 'GOOGL'

# tickerData = yf.Ticker(tickerSymbol)

# tickerDF = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')

# abc = pd.DataFrame({'asdf':['A','B','C'],'number of datasets':[3,6,2]},index=['A','B','C'])


# ax = plt.bar(x='asdf',height='number of datasets', data=abc)

# st.bar_chart(abc)
# st.line_chart(tickerDF.Close)
# st.line_chart(tickerDF.Volume)


abc = pd.DataFrame({'asdf':['A','B','C'],'number of datasets':[3,6,2]},index=['A','B','C'])


table = pd.read_excel('Dashboard.xlsx', sheet_name='DataforDashboard').iloc[3:42,2:14]

table
