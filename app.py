from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

API_key = 'BGNKZDPGRQ7RCZ7L'
def get_data(symbol,end_date,start_date):
    ts = TimeSeries(key=API_key,output_format='pandas')
    data=ts.get_monthly_adjusted(symbol)[0]
    filtered_data = data.loc[end_date:start_date]
    return filtered_data

st.write("""
# TDI Milestone Project
An interactive chart of stock closing prices using Streamlit and Bokeh.
""")
st.sidebar.header('Select plot parameters:')
ticker = st.sidebar.text_input("Ticker", 'JBLU')
start_date = st.sidebar.text_input("Start Date","2019-01-01")
end_date = st.sidebar.text_input("End Date","2020-01-01")

st.header(f"{ticker} : Open, Close, Adjusted Close, High, Low Prices" )

df=get_data(ticker,end_date,start_date)
df=df.reset_index()
df=df.sort_values(by='date')
df=df.rename(columns={'1. open':'Open','2. high':'High','3. low':'Low','4. close':'Close','5. adjusted close':'Adjusted Close'})

#fig = go.Figure(
#    data=go.Scatter(x=df['date'], y=df['Open'])
#    )
fig=px.line(df,x='date',y=df.columns[1:6])

st.plotly_chart(fig, use_container_width=True)
