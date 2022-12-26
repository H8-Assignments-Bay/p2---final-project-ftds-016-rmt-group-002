import streamlit as st
import plotly.express as px
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import seaborn as sns
import datetime
from PIL import Image

dfb1 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/ABF%20Indonesia%20Bond%20Index%20Fund%20Clean.csv')
dfb2 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/draft_model/Dataset_clean/Med%20Clean/Batavia%20Dana%20Obligasi%20Ultima%20Clean.csv')
dfb3 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/draft_model/Dataset_clean/Med%20Clean/Danamas%20Stabil%20Clean.csv')
dfb4 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Eastspring%20IDR%20Fixed%20Income%20Fund%20Kelas%20A%20Clean.csv')
dfb5 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Eastspring%20Syariah%20Fixed%20Income%20Amanah%20Kelas%20A%20Clean.csv')
dfb6 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Manulife%20Obligasi%20Negara%20Indonesia%20II%20Kelas%20A%20Clean.csv')
dfb7 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Manulife%20Obligasi%20Unggulan%20Kelas%20A.csv')
dfb8 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Schroder%20Dana%20Mantap%20Plus%20II%20Clean.csv')
dfb9 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Sucorinvest%20Sharia%20Sukuk%20Funds%20Clean.csv')
dfb10 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Med%20Clean/Sucorinvest%20Stable%20Fund%20Clean.csv')
def run():
    def user_input_low():
        low_symbol = st.sidebar.selectbox('Mutual Funds', ('ABF Indonesia Bond Index Fund',
                                                            'Batavia Dana Obligasi Ultima',
                                                            'Danamas_Stabil',
                                                            'Eastspring IDR Fixed Income Fund Kelas A',
                                                            'Eastspring Syariah Fixed Income Amanah Kelas A',
                                                            'Manulife Obligasi Negara Indonesia II Kelas A',
                                                            'Manulife Obligasi Unggulan Kelas A',
                                                            'Schroder Dana Mantap Plus II',
                                                            'Sucorinvest Sharia Sukuk Funds',
                                                            'Sucorinvest Stable Fund'))
        tickerData = yf.Ticker(low_symbol+'.JK')
        return  low_symbol
    low_symbol = user_input_low()
    if low_symbol == 'ABF Indonesia Bond Index Fund' :
        dfb1['Present'] = dfb1['Present'].astype(float)
        dfb1['date']=pd.to_datetime(dfb1['date'])
        
        fig = px.line(dfb1, x="date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    if low_symbol == 'Batavia Dana Obligasi Ultima' :

        dfb2['value'] = dfb2['value'].astype(float)
        dfb2['date']=pd.to_datetime(dfb2['date'])
        
        fig = px.line(dfb2, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Danamas_Stabil' :
        dfb3['value'] = dfb3['value'].astype(float)
        dfb3['date']=pd.to_datetime(dfb3['date'])
        
        fig = px.line(dfb3, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Eastspring IDR Fixed Income Fund Kelas A' :
        dfb4['value'] = dfb4['value'].astype(float)
        dfb4['date']=pd.to_datetime(dfb4['date'])
        
        fig = px.line(dfb4, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Eastspring Syariah Fixed Income Amanah Kelas A' :
        dfb5['Present'] = dfb5['Present'].astype(float)
        dfb5['Date']=pd.to_datetime(dfb5['Date'])
        
        fig = px.line(dfb5, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Manulife Obligasi Negara Indonesia II Kelas A' :
        dfb6['value'] = dfb6['value'].astype(float)
        dfb6['date']=pd.to_datetime(dfb6['date'])
        
        fig = px.line(dfb6, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Manulife Obligasi Unggulan Kelas A' :
        dfb7['value'] = dfb7['value'].astype(float)
        dfb7['date']=pd.to_datetime(dfb7['date'])
        
        fig = px.line(dfb7, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Schroder Dana Mantap Plus II' :
        dfb8['Present'] = dfb8['Present'].astype(float)
        dfb8['date']=pd.to_datetime(dfb8['date'])
        
        fig = px.line(dfb8, x="date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Sucorinvest Sharia Sukuk Funds' :
        dfb9['value'] = dfb9['value'].astype(float)
        dfb9['date']=pd.to_datetime(dfb9['date'])
        
        fig = px.line(dfb9, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Sucorinvest Stable Fund' :
        dfb10['value'] = dfb10['value'].astype(float)
        dfb10['date']=pd.to_datetime(dfb9['date'])
        
        fig = px.line(dfb10, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')
if __name__ == '__main__':
    run()
    