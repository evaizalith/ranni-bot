
import discord
import random 
import os
import webbrowser 
import requests 

from data.atoken import TOKEN

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command(name='greeting', help='Says hello')
async def greeting(ctx):
    print('Command: greeting')
    response = "\*bows*"
    await ctx.send(response)


@client.command(name='suggest', help='Give a suggestion')
async def suggest(ctx, *args):
    print('Command: suggest')

    try:
        suggestionFile = open("data/suggestions.txt", "a")
    except: 
        print('Failed to open suggestions.txt')
        await ctx.send("[ERROR] I can't find my notebook!")
        return 

    try: 
        content = ""

        for item in args:    
            content = content + " " + item

        suggest = "Suggestion by " + ctx.author.name + " in " + ctx.guild.name + ": " + content + "\n"
        suggestionFile.write(suggest)
        await ctx.send("Acknowledged and saved.")
    except:
        print('Suggest failed to write')
        await ctx.send("[ERROR] Your suggestion sucks and I'm not taking it.")
        return 

@client.command(name='github', help='View source code')
async def github(ctx):
    print('Command: github')
    await ctx.send("https://github.com/FoundIzalith/ranni-bot")

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
