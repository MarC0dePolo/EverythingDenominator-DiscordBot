import myChartPlotter
import re

# Function to check if the user input matches a specific pattern
def checkInput(user_message) -> bool:
    regex = r'\$plot\s-(c|n)\s(((\w|\W)+\s(\w|\W)+)|(\w|\W)+\s\/)\s(1d|5d|1mo|6mo|1y|2y|5y|10y|ytd|max)\s*(1m|2m|5m|15m|30m|90m|1h|1d|5d|1wk|1mo|3mo)'
    
    if re.match(regex, user_message):
        return True
    else:
        return False

# Function to create a C-Value plot
def getCValPlot(commands: tuple):
    # Unpack the tuple of commands
    ticker1, ticker2, period, interval = commands
    
    # Create two individual charts for each ticker
    chart1 = myChartPlotter.Chart(tickers=ticker1, period=period, interval=interval)
    chart2 = myChartPlotter.Chart(tickers=ticker2, period=period, interval=interval)
    
    # Create a C-Value chart using the two individual charts
    mainChart = myChartPlotter.CValueChart(chart1.getValueSetup(), chart1.getDataFrame(), chart2.getDataFrame())
    mainChart.plotChart(mainChart.calculateDataFrame(), f'{chart1.getName()}/{chart2.getName()}')

# Function to create a normal plot
def getNormalPlot(commands: tuple):
    # Unpack the tuple of commands
    ticker, period, interval = commands
    
    # Create a chart for the specified ticker
    mainChart = myChartPlotter.Chart(ticker, period, interval)
    mainChart.plotChart(mainChart.getDataFrame(), mainChart.getName())

# Function to determine the type of plot and call the appropriate plotting function
def getPlot(user_message):
    # Split the user message into a list of words
    p_user_message = user_message.split(' ')
    
    # Extract relevant information from the user message
    flag = p_user_message[1]
    ticker1 = p_user_message[2]
    ticker2 = p_user_message[3]
    period = p_user_message[4]
    interval = p_user_message[5]

    # If the plot should be a normal chart
    if flag == '-n' and ticker2 == '/':
        getNormalPlot((ticker1, period, interval))
    
    # If the plot should be a C-Value chart
    elif flag == '-c':
        getCValPlot((ticker1, ticker2, period, interval))