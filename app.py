from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import datetime as dt
import plotly.express as px 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import requests
import simplejson as json

API_key = 'BGNKZDPGRQ7RCZ7L'

def get_data(symbol,start_date,end_date):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey=GNKZDPGRQ7RCZ7L'
    r = requests.get(url)
    data = r.json()
    data=data['Monthly Adjusted Time Series']
    data=pd.read_json(json.dumps(data))
    data=data.transpose()
    filtered_data = data.loc[end_date:start_date]
    return filtered_data

st.write("""
# TDI Milestone Project
An interactive chart of stock closing prices using Streamlit and Plotly.
""")
st.sidebar.header('Select plot parameters:')
ticker = st.sidebar.text_input("Ticker", 'JBLU')
start_date = st.sidebar.text_input("Start Date","2019-01-01")
end_date = st.sidebar.text_input("End Date","2020-01-01")

st.header(f"{ticker} : Open, Close, Adjusted Close, High, Low Prices" )

df=get_data(ticker,start_date,end_date)
df=df.reset_index()
df=df.sort_values(by='index')
df=df.rename(columns={'index':'Date','1. open':'Open','2. high':'High','3. low':'Low','4. close':'Close','5. adjusted close':'Adjusted Close'})

fig=px.line(df,x='Date',y=df.columns[1:6])

#st.plotly_chart(fig, use_container_width=True)
