import yfinance as yf
import streamlit as sl
import pandas as pd
sl.write("""
# ***BitcoinUSDPrice App***

The **Closing price** and **volume** of Bitcoin:

""")

#Bitcoin price
symbolBitcoin = 'BTC-USD'

dataBitcoin = yf.Ticker(symbolBitcoin)

bitcoinGo = dataBitcoin.history(period = '1d', 
                                start = '2010-12-31', 
                                end = '2021-01-07')


#USD price
symbolAmerica = 'USD'

dataAmerica = yf.Ticker(symbolAmerica)

americaGo = dataAmerica.history(period = '1d',
                                start = '2010-12-31', 
                                end = '2021-01-07')




sl.line_chart(bitcoinGo.Close)
sl.line_chart(bitcoinGo.Volume)


sl.write("""
### The Closing price and volume of USD:

""")
sl.line_chart(americaGo.Close)
sl.line_chart(americaGo.Volume)

sl.write("""
Created by Anuraag Rath

""")