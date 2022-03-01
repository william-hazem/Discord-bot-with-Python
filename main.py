##
# simple discord bot

import os       # env vars
import discord  # discord api
import requests # http request
import json     # json utils

from keep_alive import keep_alive

# request random quotations
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote

# instace of discord client
client = discord.Client()
# set secret client id
client_id = os.environ['client_id']

# setting logging discord event callback
# send a message to console log when bot connect to some server
@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))

# setting chat message event callback
# register bot commands
@client.event
async def on_message(message):
    # if the message is from bot
    if message.author == client.user:
        return
        
    # read users messages
    # send "hello"
    if message.content.startswith('!Hi'):
        await message.channel.send('Hello')
    
    # send random quotations
    if message.content.startswith('!quotIEEE'):
        await message.channel.send(get_quote())

# start server
keep_alive()
# start discord client
client.run(client_id)