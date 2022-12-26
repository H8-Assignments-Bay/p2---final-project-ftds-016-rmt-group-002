import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
import low, med, high


dfp = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/Pasar%20Uang.csv')
dfb = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/Bond.csv')
dfs = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/Saham.csv')
def run():


    st.write("""
        # Trend

        Show are Corresponding Mutual Fund Trend Based On **NAV (Net Asset Value)**
        """)
    def user_input():
        stock_symbol = st.sidebar.selectbox('Category', ('Money Market', 'Bond', 'stock mutual funds'))

        tickerData = yf.Ticker(stock_symbol+'.JK')
        return  stock_symbol

    stock_symbol = user_input()
    if stock_symbol == "Money Market" :
        low.run()
        st.write("""
            # Top 10 Money Market Mutual Funds

            Show are Top 10 Money Market Mutual Fund Based On **AUM (Asset Under Management)**
            """)            
        fig = plt.figure(figsize=(15,5))
        sns.barplot(data=dfp, y="Mutual Funds", x="AUM")
        st.pyplot(fig)

    elif stock_symbol == "Bond" :
        med.run()
        st.write("""
            # Top 10 Money Market Mutual Funds

            Show are Top 10 Money Market Mutual Fund Based On **AUM (Asset Under Management)**
            """)            
        fig = plt.figure(figsize=(15,5))
        sns.barplot(data=dfb, y="Mutual Funds", x="AUM")
        st.pyplot(fig)
    else :
        high.run()
        st.write("""
            # Top 10 Money Market Mutual Funds

            Show are Top 10 Money Market Mutual Fund Based On **AUM (Asset Under Management)**
            """)            
        fig = plt.figure(figsize=(15,5))
        sns.barplot(data=dfs, y="Mutual Funds", x="AUM")
        st.pyplot(fig) 
if __name__ == '__main__':
    run()