#https://docs.streamlit.io/
#import packages
import datetime
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import streamlit as st

st.title('Market Dashboard Application')

st.sidebar.header('User Input')

def get_input():
    symbol = st.sidebar.text_input('Symbol', 'BTC-USD')
    start_date = st.sidebar.date_input('Start Date', datetime.date(2023,1,8))
    end_date = st.sidebar.date_input('End Date', datetime.date(2023,7,28))

    return symbol, start_date, end_date

def get_data(symbol, start_date, end_date):
    symbol = symbol.upper()
    if(symbol):
        df = yf.download(symbol, start=start_date, end=end_date)
    else:
        df = pd.DataFrame(['Date', 'Close', 'Open', 'Volume', 'Adj Close'])

    return df

symbol, start_date, end_date = get_input()
df = get_data(symbol, start_date, end_date)

fig = go.Figure(
    data = [go.Candlestick(
        x = df.index,
        open = df['Open'],
        high = df['High'],
        low = df['Low'],
        close = df['Close'],
        increasing_line_color = 'green',
        decreasing_line_color = 'red'
    )]
)

st.subheader('Historical Prices')
st.write(df)

st.subheader('Data Statistics')
st.write(df.describe())

st.subheader('Historical Prices Chart - Adjusted Close Price')
st.line_chart(df['Adj Close'])

st.subheader('Volume')
st.bar_chart(df['Volume'])

st.subheader('Candlestick Chart')
st.plotly_chart(fig)