import pandas as pd
from nsepy import get_history
from datetime import date
import mplfinance as mpf

TIKER = 'SBIN'
today = date.today()
data = get_history(symbol=TIKER, start=date(2020,6,1), end=today)

df1 = data[['Open', 'High', 'Low', 'Close','Volume', 'VWAP']]
df1.columns =['open', 'high', 'low', 'close', 'volume', 'VWAP']
df1.index = pd.to_datetime(df1.index, format='%Y-%m-%d')
df = df1.tail(120)

mpf.plot(df, figratio=(10, 6), type="candle",
         mav=(21), volume=True,
         title=f"Price of {TIKER}",
         tight_layout=True, style="binance")

