from discord.ext import commands
import discord
import everythingPlotterAlphaV2 as ep
import os

token = os.environ.get('DISCORD_TOKEN')
description = '''An example bot to showcase the discord.ext.commands extension'''

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# This example requires the 'message_content' intent.
bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def how(ctx):
    await ctx.send(
        '''commands:
        !give <tickers> <period> <interval>
            e.g: !give AAPL 1d 1m
        
        !give <value>/<counterValue> <period> <interval>
            e.g: !give BTC-USD/ETH-USD 1d 1m
            
        <tickers>: https://finance.yahoo.com/
        <period>: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        <interval>: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
            '''
    )

        
@bot.command()
async def give(ctx, *, message: str):
    if not bool(message.find("/")):
        message = message.split(" ")
        tickers = message[0]
        period = message[1]
        interval = message[2]
        
        chart = ep.Chart(tickers, period, interval)
        chart.plotChart(chart.getDataFrame())
    else:
        message = message.split(" ")
        tickers = message[0]
        value = tickers.split("/")[0]
        counterValue = tickers.split("/")[1]
        period = message[1]
        interval = message[2]
        chart = ep.MyCounterValueChart(
            ep.Chart(value, period, interval).getValueSetup(),
            ep.Chart(value, period, interval).getDataFrame(),
            ep.Chart(counterValue, period, interval).getDataFrame()
        )
        chart.plotChart(chart.calculateDataFrame())
    

    chart.saveChart()
    with open('chart.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)        
    
        
bot.run('token')


