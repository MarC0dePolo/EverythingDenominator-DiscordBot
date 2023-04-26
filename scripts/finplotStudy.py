# python_candlestick_chart.py

import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import yfinance as yf

def commandLaterForDiscord():
    command = input("")
    pass

def howToPlot(
    tickers,
    start=None,
    end=None,
    actions=False,
    threads=True,
    ignore_tz=None,
    group_by='column',
    auto_adjust=False,
    back_adjust=False,
    repair=False,
    keepna=False,
    progress=True,
    period="max",
    show_errors=True,
    interval="1d",
    prepost=False,
    proxy=None,
    rounding=False,
    timeout=10):

    return tickers,start, end,actions,threads,ignore_tz,\
            group_by,auto_adjust,back_adjust,repair,\
            keepna,progress,period,show_errors,interval,\
            prepost,proxy,rounding,timeout

def dataExtractionAndPlotting():
    # Extracting Data for plotting
    plt.style.use('ggplot')
    data = yf.download(howToPlot())
    data = pd.DataFrame(data)
    data.reset_index(inplace=True)
    ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
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
    fig.suptitle('Daily Candlestick Chart of NIFTY50')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()
