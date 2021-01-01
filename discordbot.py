import discord
from discord.ext import commands
import asyncio
import sys
import os.path
import random
from mutagen.mp3 import MP3

vc = None
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@bot.command()
async def sele(ctx, datName: str, num: int):
    global vc
    vc = await ctx.author.voice.channel.connect()

    if type(select(datName, num)) is list:
        dataList = select(datName, num)
        count = 0
        for musicList in dataList:
            if vc.is_playing() is False:
                audio = MP3("{}.mp3".format(musicList.rstrip('\n')))
                length = audio.info.length
                vc.play(discord.FFmpegPCMAudio('{}.mp3'.format(musicList.rstrip('\n'))))
                await asyncio.sleep(length + 5)

                
            if vc.is_playing() is False:
                count += 1

    elif type(select(datName, num)) is str:
        await ctx.send(select(datName, num))
        await ctx.voice_client.disconnect()

@bot.command()
async def stop(ctx):
    global vc
    if vc.is_playing() is True:
        vc.pause()

@bot.command()
async def resume(ctx):
    global vc
    if vc.is_paused() is True:
        vc.resume()

@bot.command()
async def dc(ctx):
    await ctx.voice_client.disconnect()

def select(listName: str, num: int):
    opFile = listName
    SelectCount = num
    count = 0
    LineCount = 0
    fileLine = 0
    random.seed()

    if os.path.isfile(opFile) == False:
        return("{0}: No such file or directory.".format(opFile))
        

    with open (opFile, "r" , encoding="utf-8_sig") as r_file:

        for music in open(opFile , encoding="utf-8_sig").readlines():
            fileLine += 1
    
    if SelectCount > fileLine:
        return("Input num is over range.")
        exit(1)

    index_set = set()
    inList = set()

    while len(index_set) < SelectCount:
        index_set.add(random.randint(1 , fileLine))

    NumberList = list(index_set)

    NumberList.sort()

    with open (opFile, "r" , encoding="utf-8_sig") as r_file:

        for music in open(opFile , encoding="utf-8_sig").readlines():
            LineCount += 1

            if LineCount == NumberList[count]:
                inList.add(music)
                count += 1

            if count == SelectCount:
                break
    
    returnList = list(inList)
    return returnList

bot.run(TOKEN)