import os 
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

INTENTS = discord.Intents(messages=True, guilds=True, reactions=True) 
INTENTS.message_content = True
client = discord.Client(command_prefix='!', intents=INTENTS)

image_dict = {
    'Chomik Padrão': 'chomikpadrao.webp',
    'Chomik Rafael Lima paladino do mal': 'chomiklima.webp',
}

chomik_list = [
        'Chomik Padrão',
        'Chomik Rafael Lima paladino do mal'
    ]


@client.event
async def on_ready():
    print(f'temporada de pescaria chomik ficará disponivel em breve, por meio do {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!ps':
        try:
            response = random.choice(chomik_list)
            image = image_dict[response]
            image_file = discord.File('images/' + image)
            await message.channel.send(response, file=image_file)
        except Exception as e: 
            await message.channel.send("Um erro ocorreu contate o Lusca Gatos")


client.run(TOKEN)
