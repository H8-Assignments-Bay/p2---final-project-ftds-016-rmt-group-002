import streamlit as st
import plotly.express as px
import yfinance as yf
import pandas as pd

dfl1 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Manulife%20Dana%20Saham%20Kelas%20A%20Clean.csv')
dfl2 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Batavia%20Dana%20Saham%20Clean.csv')
dfl3 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Sucroinvest%20Equity%20Fund%20Clean.csv')
dfl4 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Manulife%20Saham%20Andalan%20Clean.csv')
dfl5 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/BNI-AM%20Indeks%20IDX30%20Clean.csv')
dfl6 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/BNI-AM%20Inspiring%20Equity%20Fund%20Clean.csv')
dfl7 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Simas%20Saham%20Unggulan%20Clean.csv')
dfl8 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Schroder%2090%20Plus%20Equity%20Fund%20Clean.csv')
dfl9 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/Sucroinvest%20Sharia%20Equity%20Fund%20Clean.csv')
dfl10 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/High%20Clean/DanaReksa%20Mawah%20Konsumer%2010%20Kelas%20A%20Clean.csv')
def run():
    def user_input_low():
        low_symbol = st.sidebar.selectbox('Mutual Funds', ('Manulife dana saham kelas A',
                                                                'Batavia Dana Saham',
                                                                'Sucorinvest equity fund',
                                                                'Manulife Saham Andalan',
                                                                'BNI-AM Indeks IDX30',
                                                                'BNI-AM Dana Saham Inspiring Equity Fund',
                                                                'Simas Saham Unggulan',
                                                                'Schroder 90 Plus Equity Fund',
                                                                'Sucorinvest Sharia Equity Fund',
                                                                'Danareksa Mawar Konsumer 10 Kelas A'))
        tickerData = yf.Ticker(low_symbol+'.JK')
        return  low_symbol
    low_symbol = user_input_low()
    if low_symbol == 'Manulife dana saham kelas A' :
        dfl1['value'] = dfl1['value'].astype(float)
        dfl1['date']=pd.to_datetime(dfl1['date'])
        
        fig = px.line(dfl1, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    if low_symbol == 'Batavia Dana Saham' :
        dfl2['value'] = dfl2['value'].astype(float)
        dfl2['date']=pd.to_datetime(dfl2['date'])
        
        fig = px.line(dfl2, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Sucorinvest equity fund' :
        dfl3['value'] = dfl3['value'].astype(float)
        dfl3['date']=pd.to_datetime(dfl3['date'])
        
        fig = px.line(dfl3, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Manulife Saham Andalan' :
        dfl4['value'] = dfl4['value'].astype(float)
        dfl4['date']=pd.to_datetime(dfl4['date'])
        
        fig = px.line(dfl4, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'BNI-AM Indeks IDX30' :
        dfl5['value'] = dfl5['value'].astype(float)
        dfl5['date']=pd.to_datetime(dfl5['date'])
        
        fig = px.line(dfl5, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'BNI-AM Dana Saham Inspiring Equity Fund' :
        dfl6['value'] = dfl6['value'].astype(float)
        dfl6['date']=pd.to_datetime(dfl6['date'])
        
        fig = px.line(dfl6, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Simas Saham Unggulan' :
        dfl7['value'] = dfl7['value'].astype(float)
        dfl7['date']=pd.to_datetime(dfl7['date'])
        
        fig = px.line(dfl7, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Schroder 90 Plus Equity Fund' :
        dfl8['value'] = dfl8['value'].astype(float)
        dfl8['date']=pd.to_datetime(dfl8['date'])
        
        fig = px.line(dfl8, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Sucorinvest Sharia Equity Fund' :
        dfl9['value'] = dfl9['value'].astype(float)
        dfl9['date']=pd.to_datetime(dfl9['date'])
        
        fig = px.line(dfl9, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Danareksa Mawar Konsumer 10 Kelas A' :
        dfl10['value'] = dfl10['value'].astype(float)
        dfl10['date']=pd.to_datetime(dfl10['date'])
        
        fig = px.line(dfl10, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')
if __name__ == '__main__':
    run()