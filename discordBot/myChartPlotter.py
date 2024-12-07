import mplfinance as mpf
import pandas as pd
import yfinance as yf

class Chart:
    # Initialize the Chart object with tickers, period, and interval parameters
    def __init__(self, tickers, period, interval) -> None:
        self.tickers = tickers
        self.period = period
        self.interval = interval

    # Download historical OHLC data using yfinance package and return a DataFrame object
    def getDataFrame(self):
        asset = yf.Ticker(self.tickers)
        stock_data = asset.history(period=self.period, interval=self.interval)
        self.data = pd.DataFrame(stock_data)
        data = self.data
        return data

    def getValueSetup(self):
        return self.tickers, self.period, self.interval

    def getName(self):
        return self.tickers

    def plotChart(self, dataFrame, name):
        self.chart = mpf.plot(dataFrame, 
                            type='candle',
                            style='nightclouds', 
                            savefig='mega.png',
                            title=name)
                            
class CValueChart(Chart):
    def __init__(self, valueSetup, valueDataFrame : pd.DataFrame, type1, CvalueDataFrame : pd.DataFrame, type2):
        self.tickerValue, self.periodValue, self.intervalValue = valueSetup
        
        # i.e if BTC-USD / MSCI-World resize BTC-USD to MSCI-World time-index
        if type1 == 'c' and type2 == 's':
            valueDataFrame = valueDataFrame.reindex(CvalueDataFrame.index, method="ffill")
        
        elif type1 == 's' and type2 == 'c':
            CvalueDataFrame = CvalueDataFrame.reindex(valueDataFrame.index, method="ffill")

        else:
            valueDataFrame = valueDataFrame.reindex(CvalueDataFrame.index, method="ffill")

        self.valueDataFrame = valueDataFrame
        self.CvalueDataFrame = CvalueDataFrame
    
    def calculateDataFrame(self):
        return self.valueDataFrame.div(self.CvalueDataFrame)
    
if __name__ == "__main__":
    Bitcoin = Chart(tickers="BTC-USD", period="1y", interval="1wk")
    Ethereum = Chart(tickers="ETH-USD", period="1y", interval="1wk")

    #Bitcoin.plotChart(Bitcoin.getDataFrame(), Bitcoin.getName())

    btceth = CValueChart(Bitcoin.getValueSetup(), Ethereum.getDataFrame(), Bitcoin.getDataFrame())
    btceth.plotChart(btceth.calculateDataFrame(), f'{Bitcoin.getName()}/{Ethereum.getName()}') 

