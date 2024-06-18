import discord
import os
from discord.ext import commands
from server import server

intents = discord.Intents.default()
client = discord.Client(intents=intents)

intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está pronto.')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='oi')
async def oi(ctx):
    await ctx.send('Olá! Como vai?')

@bot.command(name='join')
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Você precisa estar em um canal de voz para usar este comando")
    else:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'OG Loc no canal de voz: {channel}')
        
@bot.command(name='leave')
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send('OG Loc saiu do canal de voz.')
    else:
        await ctx.send('OG Loc não está em um canal de voz.')

server()
my_secret = os.environ['TOKEN']
bot.run(my_secret)
