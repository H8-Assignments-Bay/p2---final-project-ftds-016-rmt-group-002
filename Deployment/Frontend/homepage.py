import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from PIL import Image

# Configuration
st.set_page_config(
    page_title='Profiling Questionnaries',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    
    image = Image.open('logodifa.PNG')
    st.image(image)

    st.write("""
    # Top Reksada

    Show are the stock **closing price** and **volume**
    """)

    def user_input():
        stock_symbol = st.sidebar.selectbox('Mutual Fund Category', ('Money Market', 'Bond', 'stock mutual funds'))
        date_start = st.sidebar.date_input('Start Date', datetime.date(2022, 10, 22))
        date_end = st.sidebar.date_input('End Date', datetime.date.today())

        tickerData = yf.Ticker(stock_symbol+'.JK')
        tickerDf = tickerData.history(period='1d', start=date_start, end=date_end)
        return tickerDf, stock_symbol

    input_df, stock_symbol = user_input()

    st.line_chart(input_df.Close)
    st.line_chart(input_df.Volume)

    st.write("""
    # Stock Price Prediction
    Shown are the stock prediction for next days.
    """)

if __name__ == '__main__':
    run()
