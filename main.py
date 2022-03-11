import pyjokes
import discord
import randfacts
import random
import requests
from dotenv import load_dotenv
import os

client = discord.Client()

load_dotenv()


def meme_gen():
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    fox = response.json()
    pic = fox['preview']
    meme = pic[2]
    return meme


def dog_pic():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    fox = response.json()
    print(fox)
    pic = fox['message']
    return pic


def get_joke():
    response = pyjokes.get_joke()
    return response


def get_facts():
    response = randfacts.get_fact()
    return response


def coin_toss():
    coin = random.randint(1, 100)
    if coin % 2 == 0:
        response = 'Tails'
    else:
        response = 'Heads'
    return response
    

def throw_dice():
    dice = random.randrange(1, 7)
    if dice == 6:
        response = 'Lucky you got a Six!!'
    else:
        response = dice
    return response


@client.event
async def on_ready():
    print('WE ARE LIVE!!!')
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello kind sir!,How may I help you?')

    if message.content.startswith('!joke'):
        joke = get_joke()
        await message.channel.send('Here you go:')
        await message.channel.send(joke)

    if message.content.startswith('!fact'):
        fact = get_facts()
        await message.channel.send(fact)

    if message.content.startswith('!dice'):
        dice = throw_dice()
        await message.channel.send('Throwing a dice')
        await message.channel.send(dice)

    if message.content.startswith('!dog'):
        fox = dog_pic()
        await message.channel.send(fox)

    if message.content.startswith('!meme'):
        meme = meme_gen()
        await message.channel.send(meme)
        
    if message.content.startswith('!coin'):
        coin = coin_toss()
        await message.channel.send(coin)


client.run(os.getenv('api_key'))
