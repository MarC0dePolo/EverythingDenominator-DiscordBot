import yfinance as yf
from datetime import datetime
import pandas
data = yf.download('BTC-USD', period='1mo', interval='1d')

df = pandas.DataFrame(data)
df.reset_index(inplace=True)
print(df)
