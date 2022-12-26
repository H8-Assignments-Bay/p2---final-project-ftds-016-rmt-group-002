import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image


dfl = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/final_lowrisk.csv')
dfm = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/final_medrisk.csv')
dfh = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/Final_highrisk.csv')
dfs = pd.read_csv(r'https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/raw/main/dataset_predict/final_saham.csv')
dfl=dfl.drop(['Unnamed: 0'], axis = 1)
dfm=dfm.drop(['Unnamed: 0'], axis = 1)
dfh=dfh.drop(['Unnamed: 0'], axis = 1)
dfs=dfs.drop(['Unnamed: 0'], axis = 1)

aum_low = [11.38, 2.01, 2.29, 2.07, 2.96, 4.28, 2.62, 4.9, 9.49, 3.73]
dfl['AUM'] = aum_low
aum_med = [1.51, 1.51, 1.58, 4.76, 5.57, 0.85, 2.12, 14.56, 1.29, 15.92]
dfm['AUM'] = aum_med
aum_high = [4.83, 03.02, 1.72, 3.17, 1.38, 0.62, 1.13, 0.36, 0.98, 6.18]
dfh['AUM'] = aum_high

dfm = dfm.round(decimals=2)

ls1 = {'Manulife Dana Saham Kelas A':['ADRO','ASII','BBCA','BMRI','BBNI','BBRI','GOTO','MCAS','TLKM','UNTR'],
    'Batavia Dana Saham': ['BBRI','TLKM','BMRI','BBCA','BBNI','MDKA','ADRO','KLBF','MYOR','ASII'],
    'Sucroinvest Equity Fund':['ADRO','ASII','BBRI','BBTN','BUMI','MFIN','PGAS','MYOH','TLKM','EXCL'],
    'Manulife Saham Andalan':['ADRO','BBCA','BMRI','PNBN','BBRI','GOTO','MCAS','MDKA','PNLF','TLKM'],
    'BNI-AM Indeks IDX30':['ADRO','ASII','BBCA','BBNI','BBRI','BMRI','GOTO','MDKA','TLKM','UNTR'],
    'Sucroinvest Sharia Equity Fund':['HOKI','ENAK','CSMI','ECII','ENRG','KBLI','MNCN','PGAS','MYOH','SCCO'],
    'BNI-AM Inspiring Equity Fund ':['ADRO','ASII','BBCA','BBNI','BBRI','BMRI','EXCL','SMGR','TLKM','TOWR'],
    'Simas Saham Unggulan':['ASII','BBCA','BMRI','BBNI','BBRI','ICBP','KLBF','MYOR','AMRT','TLKM'],
    'Schroder 90 Plus Equity Fund':['BBCA','BMRI','BBNI','BBRI','KLBF','MYOR','MDKA','MAPI','MLBI','TLKM'],
    'DanaReksa Mawah Konsumer 10 Kelas A':['ADRO','ASII','BBCA','BBNI','BBRI','BMRI','INCO','MEDC','MYOR','TLKM']}

dfx = pd.DataFrame(ls1)

def run ():
    st.title('Profiling Questionnaries')
    st.markdown('---')

    # Create Form

    with st.form(key='form_parameters'):
        st.subheader('A. Investment Time Horizon')
        A1 = st.selectbox('As I withdraw money from these investments, I plan to spend it over a period of...', ('10 years or more','7-9 years','4-6 years','1-3 years','Less than 1 year'))
        A2 = st.selectbox('I plan to begin taking money from my investments in...',('10 years or more', '6-10 years','3-5 years','1-2 years','1 or less than a year'))

        st.markdown('---')
        st.subheader('B. Investment Knowlegde')
        B1 = st.selectbox('When it comes to investing in stock or bond mutual funds or ETFs - or individual stocks or bonds - I would describe myself as...',('Very experienced (≥ 10 years)','Experienced (8 - 10 years)','Somewhat experienced (4 - 7 years)','Somewhat inexperienced (< 4 years)','Very inexperienced (0)'))

        st.markdown('---')
        st.subheader('C. Risk Capacity')
        C1 = st.selectbox('My purpose of investing money is...',('For the long term wealth growth','For the long term revenue and growth','Periodic income','Income and security of investment funds','Security of investment funds'))
        C2 = st.selectbox('My current and future income sources (for example, salary, social security, pensions) are...',('Very stable','Stable','Somewhat stable','Unstable','Very unstable'))
        C3 = st.selectbox('How many percent of income that will be invested?', ('> 50%','> 25%-50%', '> 10%-25%','> 0% - 10%','0%'))
        C4 = st.selectbox('How many percent of loss investment that can be beared?',('> 50%','> 25%-50%', '> 10%-25%','> 0% - 10%','0%'))

        st.markdown('---')
        st.subheader('D. Risk Attitude')
        D1 = st.selectbox('From September 2022 through October 2022, bonds lost 4%. If I owned a bond investment that lost 4% in two months, I would...', ('Sell all the remaining investment','Sell a portion of the remaining investment','Hold onto the investment and sell nothing','Buy more of the remaining investment'))
        D2 = st.selectbox('The chart shows the greatest 1-year loss and the highest 1-year gain on 3 different hypothetical investments of $10,000.* Given the potential gain or loss in any 1 year, I would invest my money in...',('EITHER a loss of $0 OR a gain of $200','EITHER a loss of $200 OR a gain of $500','EITHER a loss of $800 OR a gain of $1,200','EITHER a loss of $2,000 OR a gain of $2,500'))
        image = Image.open('Range-Outcomes.png')
        st.image(image)
        D3 = st.selectbox('Investments with higher returns typically involve greater risk.  The charts below show hypothetical annual returns (annual gains and losses) for four different investment portfolios over a 10 year period.  Keeping in mind how the returns fluctuate, which investment portfolio would you be most comfortable holding?', ('Portfolio A', 'Portfolio B','Portfolio C','Portfolio D'))
        image = Image.open('image.png')
        st.image(image)

        submitted = st.form_submit_button('Submit')

    data_inf = {
        'A1' : A1,
        'A2' : A2,
        'B1' : B1,
        'C1' : C1,
        'C2' : C2,
        'C3' : C3,
        'C4' : C4,
        'D1' : D1,
        'D2' : D2,
        'D3' : D3
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        data_inf['A1']=data_inf.A1.map({'10 years or more': 5, '7-9 years': 4,'4-6 years':3, '1-3 years':2, 'Less than 1 year':1})
        data_inf['A2']=data_inf.A2.map({'More than 8 years': 5, '7-8 years': 4,'5-6 years':3, '3-4 years':2, '1-2 years':1})
        data_inf['B1']=data_inf.B1.map({'Very experienced (≥ 10 years)': 5, 'Experienced (8 - 10 years)': 4,'Somewhat experienced (4 - 7 years)':3, 'Somewhat inexperienced (< 4 years)':2, 'Very inexperienced (0)':1})
        data_inf['C1']=data_inf.C1.map({'For the long term wealth growth': 5, 'For the long term revenue and growth': 4,'Periodic income':3, 'Income and security of investment funds':2, 'Security of investment funds':1})
        data_inf['C2']=data_inf.C2.map({'Very stable': 5, 'Stable': 4,'Somewhat stable':3, 'Unstable':2, 'Very unstable':1})
        data_inf['C3']=data_inf.C3.map({'> 50%': 5, '> 25% - 50%': 4,'> 10% - 25%':3, '> 0% - 10%':2, '0%':1})
        data_inf['C4']=data_inf.C4.map({'> 50%': 5, '> 25% - 50%': 4,'> 10% - 25%':3, '> 0% - 10%':2, '0%':1})
        data_inf['D1']=data_inf.D1.map({'Sell all the remaining investment': 0, 'Sell a portion of the remaining investment': 2,'Hold onto the investment and sell nothing':4, 'Buy more of the remaining investment':6})
        data_inf['D2']=data_inf.D2.map({'EITHER a loss of $0 OR a gain of $200': 0, 'EITHER a loss of $200 OR a gain of $500': 2,'EITHER a loss of $800 OR a gain of $1,200':4, 'EITHER a loss of $2,000 OR a gain of $2,500':6})
        data_inf['D3']=data_inf.D3.map({'Portfolio A': 0, 'Portfolio B': 2,'Portfolio C':4, 'Portfolio D':6})
        
        data_inflist=['A1','A2','B1','C1','C2','C3','C4','D1','D2','D3']
        data_inf['score'] = data_inf[data_inflist].sum(axis=1)

        # st.write('# Score: ', str(int(data_inf['score'])))
        print(type(data_inf['score'][0]),data_inf['score'])
        saham = []
        stock = []
        if data_inf['score'][0] <= 21:
            profile= 'Low Risk'
            text = 'You have a low tolerance for risk and potential loss of capital or a short investment time horizon. Investors are willing to accept some short term fluctuations and small losses in your investment portfolio in exchange for modest returns. The primary objective of your investment portfolio will be to provide income by investing primarily in funds that invest in fixed-income securities. While capital appreciation is not a priority, a small portion of the portfolio may be invested in equity funds to provide the potential for some growth to offset the impact of inflation.'
            rec1 = dfl[dfl['Label'] != 0]
            rec = rec1.sort_values(by=['AUM', 'Percentage'],ascending=False).head(3)
        elif 22 <= data_inf['score'][0] <= 36:
            profile = 'Medium Risk'
            text= ' You have a moderate tolerance for risk and loss of capital. Investors are willing to tolerate some fluctuations in your investment returns and moderate losses of capital. Investors have at least a medium term investment time horizon. The objective of investors portfolio will be to provide a combination of income and long term capital growth and therefore the portfolio will include at least 40% in fixed income investments.'
            rec1 = dfm[dfm['Label'] != 0]
            rec = rec1.sort_values(by=['AUM', 'Percentage'],ascending=False).head(3)
            rec = rec.round(decimals=2)
        elif data_inf['score'][0]  >= 37:
            profile = 'High Risk' 
            text = 'You tolerance for risk, portfolio volatility and investment losses is high or very high. Investors are willing to tolerate potentially significant and sustained price fluctuations and large losses of capital. Investors have extensive investment knowledge. Investors have no income requirements from your investments and have a long investment time horizon.'
            sh = dfs[dfs['label'] != 0]
            saham = sh.sort_values(by=['percentage'],ascending=False).head(20)
            rec1 = dfh[dfh['label'] != 0]
            rec = rec1.sort_values(by=['AUM', 'percentage'],ascending=False).head(3)
            stock = rec['saham']


        #Prediction
        st.write('# Profile Risk: {}'.format(profile))
        st.write(' {}'.format(text))
        st.write('# Our Recommendation: ')
        st.dataframe(rec.round(decimals=2))

        if len(saham) > 1:
            st.write('# Top Holding: ')
            st.dataframe(dfx[stock])
            st.write('# Top Stock: ')
            top3 = dfx[stock]
            top1 = stock.iloc[0]
            saham['saham'].isin(top3[top1]).astype(int)
            xx = saham.assign(Top=saham['saham'].isin(top3[top1]).astype(int))
            st.dataframe(xx)

if __name__ == '__main__':
    run()