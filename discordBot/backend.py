import myChartPlotter
import regex as re

def checkInput(user_message):
    pass

def getCValPlot(commands: tuple):
    ticker1, ticker2, period, interval = commands

    chart1 = myChartPlotter.Chart(tickers=ticker1, period=period, interval=interval)
    chart2 = myChartPlotter.Chart(tickers=ticker2, period=period, interval=interval)
    mainChart = myChartPlotter.CValueChart(chart1.getValueSetup(), chart1.getDataFrame(), chart2.getDataFrame())
    mainChart.plotChart(mainChart.calculateDataFrame(), f'{chart1.getName()}/{chart2.getName()}')

def getNormalPlot(commands: tuple):
    ticker, period, interval = commands
    mainChart = myChartPlotter.Chart(ticker, period, interval)
    mainChart.plotChart(mainChart.getDataFrame(), mainChart.getName())

#                                   !plot -n BTC-USD ETH-USD 1y 1wk
def getPlot(user_message):
    p_user_message = user_message.split(' ')
    flag = p_user_message[1]
    ticker1 = p_user_message[2]
    ticker2 = p_user_message[3]
    period = p_user_message[4]
    interval = p_user_message[5]

    # If Plot should be a normal Chart
    if flag == '-n' and ticker2 == '/':
        getNormalPlot((ticker1, period, interval))
    
    elif flag == '-c':
        getCValPlot((ticker1, ticker2, period, interval))
        
