import yfinance as yf
import streamlit as st
import datetime


st.write("### Quick app for importing financial graphs for a chosen company")
st.write("")
st.write("")
st.write("")
st.write("")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
st.sidebar.header('Input Parameters')
ticker_input = st.sidebar.text_input('You can choose any ticker symbol', 'AAPL')
ticker = yf.Ticker(ticker_input)
company_name = ticker.info["longName"]
st.sidebar.write(f'You chose ticker of {company_name}')
period_select = st.sidebar.selectbox('Period for fin data aproximation',('1d', '1wk', '1mo', '3mo'))
period = str(period_select)
default_start = datetime.date(2010, 1, 1)
default_end = datetime.date.today()
start = st.sidebar.date_input(label='Start date of analysis', value=default_start)
end = st.sidebar.date_input(label='End date of analysis', value=default_end)

#get the historical prices for this ticker
tickerDf = ticker.history(start=start, end=end, interval=period)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(f'###### Stock closing price of {company_name}')
st.write("")
st.line_chart(tickerDf.Close)
st.write(f'###### Stock volume of {company_name}')
st.write("")
st.line_chart(tickerDf.Volume)
st.write(f'###### Didivends per share of {company_name}')
st.write("")
st.line_chart(tickerDf.Dividends)