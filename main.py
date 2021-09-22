import os
import discord

import requests
import json

from keep_alive import keep_alive

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


client = discord.Client()
client_id = os.environ['client_id']

@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Hi'):
        await message.channel.send('Hello')

    if message.content.startswith('!quotIEEE'):
        await message.channel.send(get_quote())

keep_alive()
client.run(client_id)