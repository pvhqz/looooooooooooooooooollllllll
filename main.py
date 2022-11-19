import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)



# name = for your status and url = for your twitch link
@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "yeat /stab", url = "https://www.youtube.com/watch?v=Ud93aRpS6lI&ab_channel=MidnightArcade%E5%A4%A9%E3%81%8B%E3%82%89%E3%81%AE%E9%9F%B3"))



alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
