# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import joblib
import json
import gradio as gr

# Configuration
st.set_page_config(
    page_title='Profiling Questionnaries',
    layout='wide',
    initial_sidebar_state='expanded'
)
image = Image.open('logodifa.PNG')
st.image(image)

# Create Title
st.title('Profiling Questionnaries')
st.markdown('---')

# Create Form

with st.form(key='form_parameters'):
    st.subheader('A. Investment Time Horizon')
    A1 = st.radio('As I withdraw money from these investments, I plan to spend it over a period of...', ('10 years or more','7-9 years','4-6 years','1-3 years','Less than 1 year'))
    A2 = st.radio('I plan to begin taking money from my investments in...',('10 years or more', '6-10 years','3-5 years','1-2 years','1 or less than a year'))

    st.markdown('---')
    st.subheader('B. Investment Knowlegde')
    B1 = st.radio('When it comes to investing in stock or bond mutual funds or ETFs - or individual stocks or bonds - I would describe myself as...',('Very experienced (≥ 10 years)','Experienced (8 - 10 years)','Somewhat experienced (4 - 7 years)','Somewhat inexperienced (< 4 years)','Very inexperienced (0)'))

    st.markdown('---')
    st.subheader('C. Risk Capacity')
    C1 = st.radio('My purpose of investing money is...',('For the long term wealth growth','For the long term revenue and growth','Periodic income','Income and security of investment funds','Security of investment funds'))
    C2 = st.radio('My current and future income sources (for example, salary, social security, pensions) are...',('Very stable','Stable','Somewhat stable','Unstable','Very unstable'))
    C3 = st.radio('How many percent of income that will be invested?', ('> 50%','> 25%-50%', '> 10%-25%','> 0% - 10%','0%'))
    C4 = st.radio('How many percent of loss investment that can be beared?',('> 50%','> 25%-50%', '> 10%-25%','> 0% - 10%','0%'))

    st.markdown('---')
    st.subheader('D. Risk Attitude')
    D1 = st.radio('From September 2022 through October 2022, bonds lost 4%. If I owned a bond investment that lost 4% in two months, I would...', ('Sell all the remaining investment','Sell a portion of the remaining investment','Hold onto the investment and sell nothing','Buy more of the remaining investment'))
    D2 = st.radio('The chart shows the greatest 1-year loss and the highest 1-year gain on 3 different hypothetical investments of $10,000.* Given the potential gain or loss in any 1 year, I would invest my money in...',('EITHER a loss of $0 OR a gain of $200','EITHER a loss of $200 OR a gain of $500','EITHER a loss of $800 OR a gain of $1,200','EITHER a loss of $2,000 OR a gain of $2,500'))
    image = Image.open('Range-Outcomes.png')
    st.image(image)
    D3 = st.radio('Investments with higher returns typically involve greater risk.  The charts below show hypothetical annual returns (annual gains and losses) for four different investment portfolios over a 10 year period.  Keeping in mind how the returns fluctuate, which investment portfolio would you be most comfortable holding?', ('Portfolio A', 'Portfolio B','Portfolio C','Portfolio D'))
    image = Image.open('image.png')
    st.image(image)

    submitted = st.form_submit_button('Predict')

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

    st.write('# Score: ', str(int(data_inf['score'])))
   





