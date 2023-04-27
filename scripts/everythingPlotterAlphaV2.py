import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import yfinance as yf

# Define a Chart class for plotting candlestick charts
class Chart:
    plt.style.use('ggplot')
    
    # Initialize the Chart object with tickers, period, and interval parameters
    def __init__(self, tickers, period, interval) -> None:
        self.tickers = tickers
        self.period = period
        self.interval = interval
    
    # Download historical OHLC data using yfinance package and return a DataFrame object
    def getDataFrame(self):
        self.data = yf.download(tickers=self.tickers, period=self.period, interval=self.interval)
        self.data = pd.DataFrame(self.data)
        self.data.reset_index(inplace=True)
        data = self.data
        return data
    
    # Return the value setup (tickers, period, interval) of the Chart object
    def getValueSetup(self):
        return self.tickers, self.period, self.interval
    
    # Plot a candlestick chart using a DataFrame object containing OHLC data
    def plotChart(self, dataFrame):
        ohlc = dataFrame.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
        ohlc['Date'] = pd.to_datetime(ohlc['Date'])
        ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
        ohlc = ohlc.astype(float)
        
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        fig.suptitle(None)

        # Formatting Date
        date_format = mpl_dates.DateFormatter('%d-%m-%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()
        fig.tight_layout()
        plt.show()

# Define a subclass of the Chart class for plotting the value of two Charts
class MyCounterValueChart(Chart):
    # Initialize the MyCounterValueChart object with the value setup and DataFrame objects for Ethereum and Bitcoin
    def __init__(self, valueSetup, valueDataFrame, CvalueDataFrame):
        self.tickerValue, self.periodValue, self.intervalValue = valueSetup
        self.valueDataFrame = valueDataFrame
        self.CvalueDataFrame = CvalueDataFrame
    
    # Calculate the value of two assets divide it by the 
    # counter value and return a DataFrame object for plotting
    def calculateDataFrame(self):
        # Divide asset by the counter asset 
        # and return OHLC data for each column beeing ['Open', 'High', 'Low', 'Close']
        myChart = pd.DataFrame(self.valueDataFrame.loc[:, ['Open', 'High', 'Low', 'Close']]/self.CvalueDataFrame.loc[:, ['Open', 'High', 'Low', 'Close']])
        dates = self.CvalueDataFrame.loc[:, ['Date']]
        myChart = pd.concat([dates, myChart], axis=1)
        return myChart
