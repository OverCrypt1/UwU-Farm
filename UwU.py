import random as ultimatejija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import asyncio as made_by_ultimate
import difflib
token = ("") 
ultimateop = discord.Intents.all()
ultimateyy = (".")
ultimate = commands.Bot(command_prefix=ultimateyy,
                        case_insensitive=True,
                        self_bot=True,
                        intents=ultimateop); ultimate.remove_command("help")
running = True
pray_loop_running = True
print(
    f"""\n\n\n\n\n\n\n{Fore.BLUE} █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
{Style.RESET_ALL}""")

init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By ultimate <3{Style.RESET_ALL}")


@ultimate.event
async def on_ready():
    print(
        f"{Fore.LIGHTRED_EX} > U L T I M A T E S3LFBOT Connected To:{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}{ultimate.user}{Style.BRIGHT}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX} > Minor Updates And Fixes{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX} > Special Thanks To Async x Cosmic Development <3{Style.RESET_ALL}")
    ultimate.loop.create_task(auto_gems())

@ultimate.command(aliases=["h"])
async def help(ctx):
    ultimate_help = """
🤑 **ultimate OwO Farm V2.2** 🤑 
Prefix: `.`

**__Main__**
🌟 **Start:** *Starts The AutoBot*
🛑 **Stop:** *Stops The AutoBot*

**__Features__**
⚠ **Ban Bypass**
🚨 **Auto Detects OwO Warnings**
⏱ **Auto Cut After 1 Warning**
💎 **Auto Use Gems every 15 minutes** 
🏹 **Fast And Secure**

**__Made with 💖 and 🧠 by ultimate__** 
"""
    await ctx.send(ultimate_help)

async def auto_gems():
    await ultimate.wait_until_ready()  
    channel_id = 1263766797774225420 
    while not ultimate.is_closed():
        channel = ultimate.get_channel(channel_id)
        if channel:
            await channel.send("idhar mera gems ka naam dalo bc")  
        await made_by_ultimate.sleep(900)

@ultimate.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        command = ctx.message.content.split()[0][1:]  
        commands_list = [cmd.name for cmd in ultimate.commands]
        similar_commands = difflib.get_close_matches(command, commands_list, n=3, cutoff=0.5)

        if similar_commands:
            suggestion = ", ".join(similar_commands)
            await ctx.send(f"Command not found. Did you mean: {suggestion}?")
        else:
            await ctx.send("Command not found. Type `.help` to see a list of available commands.")
    else:
        raise error


@ultimate.command()
async def start(ctx):
    global running
    running = True
    while True:
        if not running:
            break

        await ctx.send(ultimatejija.choice(["owo hunt", "owo h"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        await ctx.send(ultimatejija.choice(["owo battle", "owo b"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        await ctx.send(ultimatejija.choice(["owo cf 1", "owo s 1"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        await ctx.send(ultimatejija.choice(["owo cookie", "owo q"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        await ctx.send(ultimatejija.choice(["owo pray", "owo clover"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        await ctx.send(
            ultimatejija.choice(["owo inv", "owo owo", "owo xp", "owo z"]))
        await made_by_ultimate.sleep(
            ultimatejija.choice([6, 5.2, 4.2, 7.3, 8.9, 3.5, 3, 4.7]))

        phrases = [
            "ughhh am bored", "hell naaaaa", "lemme grind some moree",
            "To-do list: 1. Talk to myself, 2. Repeat", "ayo what", "dang it",
            "nuh uhhh", "i gotta do this",
            "If I were a superhero, my power would be the ability to find lost socks"
        ]
        await ctx.send(ultimatejija.choice(phrases))
        latest_messages = await ctx.channel.history(limit=10).flatten()
        for message in latest_messages:
            if "please complete your captcha" in message.content.lower() or "please solve the captcha" in message.content.lower():
                await ctx.send("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                print("⚠ Warning Detected! 🛑 Stopping The Process | Type .start again to re-start grinding")
                running = False
                break

@ultimate.command()
async def stop(ctx):
    global running
    running = False
    await ctx.send("⭕Process Stopped")


ultimate.run(token, bot=False)
