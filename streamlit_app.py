import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np
import streamlit as st
 
 
 
 
st.title('Crypto price over time.')
 
 
with st.form(key='my_form'):
    crypto=st.selectbox('Select Cryptocurrency', ['BTC','ETH','XRP','BCH'])
    start=st.date_input('Start')
    end=st.date_input('End')
    submit_button = st.form_submit_button(label='Submit')
 
if submit_button:
    df = web.DataReader(f'{crypto}-USD', 'yahoo', start, end)
 
    st.line_chart(df['Adj Close'])