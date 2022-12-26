import streamlit as st
import plotly.express as px
import yfinance as yf
import pandas as pd

dfl1 = pd.read_csv(r'https://raw.githubusercontent.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/main/Dataset_clean/Low%20Clean/Bahana%20Dana%20Likuid%20Clean.csv')
dfl2 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Batavia%20Dana%20Kas%20Maxima%20Clean.csv')
dfl3 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/BNI%20AM%20Dana%20Likuid%20Clean.csv')
dfl4 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Danamas_rupiah_plus%20Clean.csv')
dfl5 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Danareksa%20Seruni%20Pasar%20Uang%20II%20Clean.csv')
dfl6 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Manulife_dana_kas_kelas_A%20Clean.csv')
dfl7 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Sucorinvest%20Money%20Market%20Fund%20Clean.csv')
dfl8 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Danareksa%20Seruni%20Pasar%20Uang%20III.csv')
dfl9 = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/Dataset_clean/Low%20Clean/Sukorinvest%20Sharia%20Money%20Market%20Fund%20Clean.csv')
dfl10 = pd.read_csv(r'https://raw.githubusercontent.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/main/Dataset_clean/Low%20Clean/TRIM%20Kas%202%20Clean.csv')
def run():
    def user_input_low():
        low_symbol = st.sidebar.selectbox('Mutual Funds', ('Batavia Dana Kas Maxima',
                                                                'Sucorinvest Money Market Fund',
                                                                'Bahana Dana Likuid',
                                                                'Manulife Dana Kas II Kelas A',
                                                                'TRIM Kas 2',
                                                                'Danareksa Seruni Pasar Uang III',
                                                                'Sucorinvest Sharia Money Market Fund',
                                                                'Danamas Rupiah Plus',
                                                                'Danareksa Seruni Pasar Uang II',
                                                                'BNI-AM Dana Likuid'))
        tickerData = yf.Ticker(low_symbol+'.JK')
        return  low_symbol
    low_symbol = user_input_low()
    if low_symbol == 'Batavia Dana Kas Maxima' :

        fig = px.line(dfl2, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')


    elif low_symbol == 'Sucorinvest Money Market Fund' :
        dfl7['Present'] = dfl7['Present'].astype(float)
        dfl7['Date']=pd.to_datetime(dfl7['Date'])

        fig = px.line(dfl7, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Bahana Dana Likuid' :

        dfl1['Present'] = dfl1['Present'].astype(float)
        dfl1['Date']=pd.to_datetime(dfl1['Date'])
        
        fig = px.line(dfl1, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Manulife Dana Kas II Kelas A' :
        dfl6['value'] = dfl6['value'].astype(float)
        dfl6['date']=pd.to_datetime(dfl6['date'])
        
        fig = px.line(dfl6, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'TRIM Kas 2' :
        dfl10['Present'] = dfl10['Present'].astype(float)
        dfl10['Date']=pd.to_datetime(dfl10['Date'])
        
        fig = px.line(dfl10, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Danareksa Seruni Pasar Uang III' :

        dfl5['Present'] = dfl5['Present'].astype(float)
        dfl5['Date']=pd.to_datetime(dfl5['Date'])
        
        fig = px.line(dfl5, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Sucorinvest Sharia Money Market Fund' :
        dfl9['Present'] = dfl9['Present'].astype(float)
        dfl9['Date']=pd.to_datetime(dfl9['Date'])
        
        fig = px.line(dfl9, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Danamas Rupiah Plus' :
        dfl4['value'] = dfl4['value'].astype(float)
        dfl4['date']=pd.to_datetime(dfl4['date'])
        
        fig = px.line(dfl4, x="date", y="value")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'Danareksa Seruni Pasar Uang II' :

        fig = px.line(dfl5, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')

    elif low_symbol == 'BNI-AM Dana Likuid' :
        dfl3['Present'] = dfl3['Present'].astype(float)
        dfl3['Date']=pd.to_datetime(dfl3['Date'])
        
        fig = px.line(dfl3, x="Date", y="Present")
        fig.update_traces(textposition="bottom right")
        st.plotly_chart(fig)
        st.markdown('---')
if __name__ == '__main__':
    run()