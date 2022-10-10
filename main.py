import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

from emojis import EMOJI_NUM, EMOJI_UTIL
from sondage import send_msg

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
serverId = os.getenv("SERVER_ID")
clientId = os.getenv("CLIENT_ID")

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("Botomploy is up")

@client.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")

@client.command(name="vjam")
async def sondage(ctx, *props):
    await send_msg(ctx, client, props)

client.run(token)
