import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix="!") #or your prefix

@bot.event
async def on_ready():
    print("Bot connected")

    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Any game"))


@bot.command(aliases=['clean', 'delmsgs'])
@commands.has_permissions(manage_messages = True)
async def clear( ctx, limit = 100 ): # or any limit you like
    await ctx.channel.purge( limit = limit )
    await ctx.send('Cleared the chat')

bot.run("Your bot's token")    
