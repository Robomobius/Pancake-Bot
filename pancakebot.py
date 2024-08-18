import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, activity = discord.Activity(name='my pancakes cook', type=discord.ActivityType.watching), command_prefix='/')

pancaketexts = ["Yum yum!","Delicious!","I love me some pancakes","Here you are!","Eat up!","Mmmmmm","Flapjack moment","Certified flipper","🥞🥞🥞🥞🥞","I downloaded all these images from google","Syrupy syrup! It reminds me of something...","Flapjack or pancake?","Coming right up!","Do you prefer waffles or pancake?","pancakes are better than waffles"]

#------------------------------------------------------

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'hi ' in (message.content.lower()+" ") or 'hello' in message.content.lower() or 'hi!' in message.content.lower():
        await message.channel.send('Hi! Have a pancake!')
        await message.channel.send(':pancakes:')

    if ('😭') in message.content or ('🥹') in message.content.lower() or ('😢') in message.content.lower():
        await message.channel.send('You are sad. Have a pancake.')
        await message.channel.send(':pancakes:')

    if ('pancake') in message.content.lower() and not('hi' in (message.content.lower()) or 'hello' in message.content.lower() or "more" in message.content.lower() or ('😭') in message.content or ('🥹') in message.content.lower() or ('😢') in message.content.lower()):
        await message.channel.send('🥞🥞🥞')

    if ('bruh') in message.content.lower():
        await message.channel.send('💀💀🥞💀')

    if ('yay') in message.content.lower() or ('birthday') in message.content.lower() or ('bday') in message.content.lower():
        await message.channel.send('🥳🤖🎉🥞🥞🥞🧇')

    if 'fuck' in message.content.lower() or 'shit' in message.content.lower() or 'bitch' in message.content.lower() or 'pussy' in message.content.lower() or 'nigger' in message.content.lower():
        await message.author.send('No swear or no more pancakes')
        await message.author.send('>:(')

    if random.randint(1,10) == 1:
        await message.add_reaction('\N{PANCAKES}')

    if ('bye') in message.content.lower():
        await message.channel.send('Bye! 👋🥞')

    if ('more') in message.content.lower():
        await message.channel.send('🥞🥞🥞🥞🥞')

@bot.tree.command(name="pancake", description="Gimmie a pancake pic")
async def _pancakecmd(ctx):
    await ctx.response.send_message(pancaketexts[random.randint(1,len(pancaketexts)-1)], file=discord.File("pictures/" + str(random.randint(1,38)) + '.jpg'))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("ready")

#------------------------------------
bot.run(open('token', 'r').read())