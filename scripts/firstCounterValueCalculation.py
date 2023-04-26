import pandas as pd
import yfinance as yf

df1 = yf.download('BTC-USd', interval="1d", period="1mo")
df2 = yf.download('ETH-USD', interval="1d", period="1mo")
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)
df1.reset_index(inplace=True)
df2.reset_index(inplace=True)

df3 = pd.DataFrame(df1.loc[:, ['Open', 'High', 'Low', 'Close']]/df2.loc[:, ['Open', 'High', 'Low', 'Close']])

dates = df1.loc[:, ['Date']]
df3 = pd.concat([dates, df3], axis=1)
print(df3)
