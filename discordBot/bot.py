import discord
import responses
import backend
import mytoken
import traceback

# Asynchronous function to send messages based on user input
async def send_message(message, user_message):
    try:
        if user_message[0] == '$':
            # If the input is a valid plot command, generate and send the plot image
            if backend.checkInput(user_message):
                backend.getPlot(user_message)
                await message.channel.send(file=discord.File('mega.png'))
            
            # If the input is a help command, send the help response
            elif '$help' in user_message:
                response = responses.help_response(user_message)
                await message.channel.send(response)
            
            # If the input is neither a valid plot command nor a help command, send an error response
            else:
                
                await message.channel.send(responses.wrong_input_response())

    except Exception as e:
        print(e)
        traceback.print_exc()

# Function to run the Discord bot
def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Print the received message details to the console
        print(f'{username} said: {user_message} ({channel})')

        # Process the message and send appropriate responses
        await send_message(message, user_message)            

    client.run(mytoken.TOKEN)
