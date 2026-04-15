import discord
import os 
from discord.ext import commands
from data import CHALLENGES


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
users = {

}

challenges1 = list(CHALLENGES.keys())

def user_create(userid, name):
    if userid not in users:
        users[userid] = {
            "name" : name,
            "points" : 0,
            "level" : 1,
            "ac_challenge" : 0
        } 

def levelcalc(points):
    if points == 19:
        return 4
    elif points >= 12:
        return 3
    elif points >= 7:
        return 2
    else:
        return 1

def uptlevel(userid):
    user_point = users[userid]["points"]
    levels = levelcalc(user_point)
    users[userid]["level"] = levels

def actualchallenge(userid):
    act = users[userid]["ac_challenge"]
    if act < len(challenges1):
        key_chall = challenges1[act]
        return key_chall, CHALLENGES[key_chall]
    else:
        return None, None

def challengeup(userid):
    users[userid]["ac_challenge"] += 1

# def levelz(userid):
    # if CHALLENGES []:
    
@bot.event
async def on_ready():
    print(f"a sus ordenes mi general")

@bot.command()
async def profile(ctx):
    user_id = str(ctx.author.id)
    names = ctx.author.mention
    user_create(user_id, names)
    user = users[user_id]
    await ctx.send(f" Profile of {user["name"]}\n Points : {user["points"]}\n Levels : {user["level"]}")

@bot.command()
async def hi(ctx):
    with open("environmental-issues1.png", "rb") as file:
        image = discord.File(file)
    await ctx.send(f"Hello!, I am Greenpath, a bot related to Enviromental issues and climate change.\n ")
    await ctx.send(file = image)


@bot.command()
async def challenge(ctx): 
    userid = str(ctx.author.id)
    name = ctx.author.name
    user_create(userid, name)
    keychall, act_chall = actualchallenge(userid)
    if act_chall is None:
        await ctx.send("Congratulations! You have completed all the challenges in your way!!")
        return 
    options = act_chall["options"]
    options_text = (
    "A) " + options[0] + "\n"
    "B) " + options[1] + "\n"
    "C) " + options[2] + "\n"
    "D) " + options[3]
    )

    await ctx.send(f"Challenge: {act_chall["title"]}\n Question: {act_chall["question"]}\n Options =\n {options_text} \n Choose and type between the options (A), (B), (C) and (D)")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for("message", timeout= 30.0, check=check)
        answer = msg.content.upper()
        if answer not in ["A", "B", "C", "D"]:
            await ctx.send("That is not a answer, please use A, B, C or D to answer")
            return
        
        selected_option = ""
        if answer == "A":
            selected_option = options[0]
        elif answer == "B":
            selected_option = options[1]
        elif answer == "C":
            selected_option = options[2]
        elif answer == "D":
            selected_option = options[3]

        if selected_option == act_chall["answer"]:
            users[userid]["points"] += act_chall["points"]
            uptlevel(userid)
            newlv = users[userid]["level"] 
            challengeup(userid)

            message = (
                f"✅ Correct, {ctx.author.mention}!\n"
                f"You earned **{act_chall['points']} points**.\n"
                f"💰 Total points: **{users[userid]['points']}**\n"
                f"🏆 Current level: **{users[userid]['level']}**"
            )
            await ctx.send(message)
#            oldlv = users[userid["level"]]
#            if newlv > oldlv:
#                message += f"\n You have leveled up"
         
        else:
            await ctx.send("Incorrect! Try again.")
    except:
        await ctx.send("Times over! You must complete the question within 30 seconds. Try again.")

bot.run("")