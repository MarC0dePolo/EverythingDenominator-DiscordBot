help_message = """
`-------Plot a Chart------

Plot Normal Chart:
$plot [-n] [ticker] [/] [period] [interval]
i.e:  $plot -n BTC-USD / 1y 1wk

Chart with choosen counter value:
plot [-c] [ticker1/[type]] [ticker2/[type]] [period] [interval]
i.e:  $plot -c MSTR/s BTC-USD/c 1y 1wk

/s stands for stock or weekend closing asset
/c stands for crypto asset

spaces are the seperator
    
Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

Find valid ticker symbols here:
>>> https://finance.yahoo.com/ <<<`"""
