# Make me a Discord Bot which bans anybody who talks about "soup"
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if "soup" in message.content:
        await bot.ban(message.author)

bot.run('token')
