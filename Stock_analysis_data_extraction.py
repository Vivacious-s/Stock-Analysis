import yfinance as yf
import pandas as pd

'''tesla=yf.Ticker("TSLA")
tesla_data=tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.to_csv("Tesla_data.csv",index=False)'''

gme=yf.Ticker("GME")
gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.to_csv("GME_data.csv",index=False)