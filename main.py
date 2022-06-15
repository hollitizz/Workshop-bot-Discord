from discord.ext import commands
import discord


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="YOUR_PREFIX_HERE", intents=intents)


@bot.command()
async def ping(ctx):
    # await ctx.reply("Pong!")
    await ctx.send("Pong!")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready !")


bot.run("YOUR_TOKEN_HERE")
