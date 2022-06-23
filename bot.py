# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
import json

import lets_cloud

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='*')

@bot.command(name='details', help='Shows details about the instance')
async def start(ctx):
    response = lets_cloud.instance_details()
    await ctx.send('```' + response.text + '```')

@bot.command(name='power-on', help='Powers On the instance')
async def start(ctx):
    response = lets_cloud.instance_power_on()
    await ctx.send('```' + response.text + '```')

@bot.command(name='power-off', help='Powers Off the instance')
async def start(ctx):
    response = lets_cloud.instance_power_off()
    await ctx.send('```' + response.text + '```')

@bot.command(name='reboot', help='Reboots the instance')
async def start(ctx):
    response = lets_cloud.instance_reboot()
    await ctx.send('```' + response.text + '```')

bot.run(TOKEN)