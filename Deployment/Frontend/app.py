import streamlit as st
import homepage
import predict

navigation = st.sidebar.selectbox('Page :', ('Home', 'Profiling Questionnaries'))
if navigation == 'Home':
    homepage.run()
else:
    predict.run()