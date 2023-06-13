import discord 
import message_handle
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_KEY = os.getenv('DISCORD_KEY')

intentss = discord.Intents.default() #dunno what it does
intentss.message_content = True #dunno what it does


async def send_message(message,user_message):
    try:
        response = message_handle.message_handle(user_message)
        await message.channel.send(response)
    except:
        await message.channel.send("Oops, I didn't get shit, I might be having some issues")


def run_bridget():

    Bridget_client=discord.Client(intents=intentss)

    @Bridget_client.event
    async def on_ready():
        print('BRIDGET IS READY')
        

    @Bridget_client.event
    async def on_message(message):
        if message.author==Bridget_client.user:
            return 

        user_message=message.content
        Important_message=user_message[8:]


        if type(message.channel)==discord.channel.DMChannel:
            await send_message(message,user_message)
        else:
            if user_message[0:8]=='Bridget:':
                await send_message(message, Important_message)





    Bridget_client.run(DISCORD_KEY)
        


