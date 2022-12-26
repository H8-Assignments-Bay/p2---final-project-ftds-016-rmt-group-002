import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from PIL import Image
import Home, Prediction


pageicon = Image.open('logodifa-removebg-preview.png')
home1=Image.open('images-icone.png')
home2=Image.open('clipart-computer-icons.png')
home3=Image.open('image.png')

st.set_page_config(page_title = 'Your personal Digital Financial Advisory for Mutual Funds',page_icon=pageicon, layout='wide', initial_sidebar_state='expanded')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.discordapp.com/attachments/554269836650348566/1054983902168629309/logodifa-removebg-preview.png");
             background-attachment: fixed;
             background-size: 5%;
             background-color: Transparent;
             background-repeat: no-repeat;
             background-position: 100% 7%;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

header = Image.open('logodifa-removebg-preview.png')
header2 = Image.open('images-icone.png')
# header2 = header2.resize((1300,300))

st.subheader('Your personal Digital Financial Advisory for Mutual Funds')
st.write('-----')

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home', 'Profile Risk'],
        icons=['house','cash'],
        menu_icon='cast',
        default_index=0,       
    )

if selected == 'Home':
    Home.run()

elif selected == 'Profile Risk':
    Prediction.run()