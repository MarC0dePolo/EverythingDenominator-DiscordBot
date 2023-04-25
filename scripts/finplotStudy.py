import finplot as fplt
import yfinance
df = yfinance.download('BTC-USD', period='1mo', interval='1d')
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
name = "AAPL_test.png"
fplt._savewindata(name)
fplt.show()
 