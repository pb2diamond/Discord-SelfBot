#discord bot made by pb2 diamond
#diamond pb2 - youtube
#@pb2 diamond#1544 - discord
 
##IMPORTS##
import discord                      #MAKE SURE YOU DO "py -m pip install discord" IN COMMAND PROMPT!
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
import random

##PREFIX##
bot = commands.Bot(command_prefix='++')

##BOT IS READY## 
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Execute Commands")
    print ("Logged In As")
    print (bot.user.name)
    print (bot.user.id)
 
##COMMAND##
@bot.command(pass_context=True)
async def testbot(ctx): #run "++testbot" to run the command
    if True:
        await bot.say("Bot Is Online!") #NOTE - you need the \n (new lines)
      
##COMMAND##
@bot.command(pass_context=True)
async def insta(ctx): #run "++insta" to run the command
    if True:
        await bot.say("Instructions:\n++testbot\n++insta\n++attack\n++ping\n++yes_no") #NOTE - you need the \n (new lines)

##COMMAND##
@bot.command(pass_context=True)
async def attack(ctx): #run "++punch" to run the command
    if True:
        await bot.say("https://media.discordapp.net/attachments/477121368199135263/482580605272457246/fight_action.gif\n") #NOTE - you need the \n (new lines)
       
##COMMAND##
@bot.command(pass_context=True)
async def ping(ctx): #run "++ping" to run the command
    if True:
        await bot.say(":ping_pong: Ping!!!!") #NOTE - you need the \n (new lines)
       
##COMMAND##
@bot.command(pass_context=True)
async def yes_no():
    possible_responses = [ 'Yes Definitely','No Never','Possibly','Possibly Not','I Cannot Answer Your Question','I Am Not Sure','Maybe','Yes','No','Its Yes','Of Course Not','Its No','Too Hard To Tell','It Is Hard To Answer That Question' ]
    await bot.say(random.choice(possible_responses))
 
##COMMAND##
@bot.command(pass_context=True)
async def info(ctx): #run "++info" to run the command
    if True:
        embed=discord.Embed(title="What Is Pb2 (Plazma Burst 2)?", description="Plazma Burst 2 Is A Sidescrolling 2d Shooter Where A Marine Crashes Into A Planet And Fights Off Aliens.")
        embed.add_field(name="Extra Info", value="If You Would Like To Check Out Pb2 Go To https://www.plazmaburst2.com/")
        await bot.say(embed=embed)

##COMMAND##
@bot.command(pass_context=True)
async def givecookie(ctx, user: discord.Member): #run "++givecookie" to run the command
    if True:
        userID = user.id
        await bot.say("Given A Cookie To <@user>") #NOTE - you need the \n (new lines)
     
    
##BOT TOKEN##
bot.run ("NDc2MDUwMTMyOTk2MDYzMjMy.DmhApA.p2gRgCyB1APn_1IXjBJNcIusQP8")
