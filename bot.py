import discord 
import responses
import discord, random
from discord.ext import commands



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        


def run_discord_bot():
    TOKEN = 'MTAzOTkxMTgxNjg5MDk1Nzg1NA.GbJCHO.R8Vqxm3Iyrz5ZTRy6qsp_sAEorWdHdJd3AVSOQ'  # bot token
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running' )   #po spuštění bot napíše "<name> is now running"
              
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")   #prin zpráv ze serveru do terminálu
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)   # private messages

    
    client.run(TOKEN)