import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

buzz_words = ["fuck", "shit", "cock", "asshole", "periodt", "period", "bruh", "lmao", "stink"]

buzz_response = [
  "i hate my life",
  "i dont wanna do this anymore",
  "GETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEADGETOUTOFMYHEAD",
  "i fucking hate kids",
  "who the fuck cares",
  "everyone is so cringe",
  "just shut up",
  "god dont you people just shut up",
  "holy fuck i hate it here",
  "fuck you, shitters",
  "where the fuck am i",
  "you are literally the definition of cringe",
  "im better than you",

]

def get_quote():
  return("youre cringe dude")

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith("&anime"):
    await message.channel.send(
"⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄\n"
" ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄\n"
"⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄\n"
"⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄\n"
"⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰\n"
"⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤\n"
"⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗\n"
"⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄\n"
"⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄\n"
"⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄\n"
"⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄\n"
"⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄\n"
"⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄\n"
"⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴\n"
"⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿")

  if msg.startswith("&amogus"):
    await message.channel.send(
"⣿⣿⣿⠟⢹⣶⣶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⡟⢰⡌⠿⢿⣿⡾⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⢸⣿⣤⣒⣶⣾⣳⡻⣿⣿⣿⣿⡿⢛⣯⣭⣭⣭⣽⣻⣿⣿⣿\n"
"⣿⣿⣿⢸⣿⣿⣿⣿⢿⡇⣶⡽⣿⠟⣡⣶⣾⣯⣭⣽⣟⡻⣿⣷⡽⣿\n"
"⣿⣿⣿⠸⣿⣿⣿⣿⢇⠃⣟⣷⠃⢸⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽\n"
"⣿⣿⣿⣇⢻⣿⣿⣯⣕⠧⢿⢿⣇⢯⣝⣒⣛⣯⣭⣛⣛⣣⣿⣿⣿⡇\n"
"⣿⣿⣿⣿⣌⢿⣿⣿⣿⣿⡘⣞⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
"⣿⣿⣿⣿⣿⣦⠻⠿⣿⣿⣷⠈⢞⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
"⣿⣿⣿⣿⣿⣿⣗⠄⢿⣿⣿⡆⡈⣽⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻\n"
"⣿⣿⣿⣿⡿⣻⣽⣿⣆⠹⣿⡇⠁⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾\n"
"⣿⠿⣛⣽⣾⣿⣿⠿⠋⠄⢻⣷⣾⣿⣧⠟⣡⣾⣿⣿⣿⣿⣿⣿⡇⣿\n"
"⢼⡟⢿⣿⡿⠋⠁⣀⡀⠄⠘⠊⣨⣽⠁⠰⣿⣿⣿⣿⣿⣿⣿⡍⠗⣿\n"
"⡼⣿⠄⠄⠄⠄⣼⣿⡗⢠⣶⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣇⢠⣿\n"
"⣷⣝⠄⠄⢀⠄⢻⡟⠄⣿⣿⣿⣿⠃⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⢹⣿\n"
"⣿⣿⣿⣿⣿⣧⣄⣁⡀⠙⢿⡿⠋⠄⣸⡆⠄⠻⣿⡿⠟⢛⣩⣝⣚⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣾⣿⣿⣄⠄⠄⠄⣴⣿⣿⣿⣇⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠛⠿⣿⣫⣾⣿")

  if msg.startswith("im so smart"):
    await message.channel.send("hes pretty smart\n", file=discord.File("pic.png"))

  if msg.startswith("&eddy"):
    await message.channel.send("eddy had diva\n", file=discord.File("diva.png"))

  if msg.startswith("&alan"):
    await message.channel.send("fuck me, that guy needs a life")

  if msg.startswith("&jordan"):
    await message.channel.send("DUHHH CIRNGE!!!! DUHHH BRINGE!!???!!1 CRINGE!!!!! IS THAT ALL YOU SHITPOSTING FUCKS CAN SAY!!??? DURR BASED BASED BASED CRINGE CRINGE BASED BASED CRINGE CRINGE CRINGE BASED CRINGE I FEEL LIKE IM IN A FUCKING ASYLUM FULL OF DEMENTIA RIDDEN OLD PEOPLE THAT CAN DO NOTHING BUT REPEAT THE SAME FUCKING WORDS ON LOOP LIKE A FUCKING BROKEN RECORD CRINGE CRINGE CRINGE BASED BASED CRINGE ONIONS ONIONS ONIONS SNOYY ONIONS LOL ONIONS!!! CRINGE!!!1 BOOMER!! LE ZOOMER!!!! I AM BOOMER!!!! NO ZOOM ZOOM ZOOMIES ZOOMER GOING ZOOMIES AHGHGH I FUCKING HATE THE INTERNET SO GODDAMN MUCH FUCKJK YOU SHITPOST I HONEST TO GOD HOPE YOUR MOTHER CHOKES ON HER OWN FECES IN HELL YOU COCKSUCKER VUT OHHH I KNOWM MY POST IS CRINGE ISNT IT?? CRINGE CRINGE CRINGR CRINGEY BASED CRINGE BASED REDDIT REDDIT CRINGE ZOOM CRINGE ONIONS REDDIT BASED BASED!!!!!!")

  if msg.startswith("stfu"):
    await message.channel.send("i didnt ask for your opinion shit head")
    
  if msg.startswith("brb"):
    await message.channel.send("dont come back")

  if msg.startswith("gn"):
    await message.channel.send("dont wake up")

  if msg.startswith("&albert"):
    await message.channel.send("i love him so much")

  if msg.startswith("&helen"):
    await message.channel.send(file = discord.File("Cheesecat.png"))

  if db["responding"]:
    options = buzz_response
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in buzz_words):
      await message.channel.send(random.choice(options))

    if msg.startswith("&cmdlist"):
      await message.channel.send("&albert &alan &anime\n&eddy &jordan &helen\n&amogus &clips &brodie")

  if msg.startswith("&responding"):
    value = msg.split("&responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  @client.command()
  async def embed(ctx):
    embed=discord.Embed(title="im a genius", url="reversah.com", description="im actually so smart", color=0x000000)
    await ctx.send(embed=embed)

  embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData",   icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")

  embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

  embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False) 
  embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
  embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)

  embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")

keep_alive()
client.run(os.getenv("TOKEN"))