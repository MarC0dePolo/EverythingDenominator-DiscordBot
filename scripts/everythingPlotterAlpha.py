import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
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

ohlc = df3.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

# Creating Subplots
fig, ax = plt.subplots()

# plot width with a dict depending on interval scale
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Candlestick Chart of SELHOF')

# Formatting Date
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

plt.show()
