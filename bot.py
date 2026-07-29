import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Your server's channel IDs
WELCOME_CHANNEL_ID = 1532028426091757569
RULES_CHANNEL_ID = 1532029711692071074

@bot.event
async def on_ready():
    print(f'Bot is successfully logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    
    if channel:
        rules_channel_mention = f"<#{RULES_CHANNEL_ID}>"
        
        embed = discord.Embed(
            title="Welcome to the Server! 🎉",
            description=f"Hello {member.mention}! We are so glad to have you here.\nPlease make sure to check out the rules in {rules_channel_mention} and enjoy your stay!",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        
        await channel.send(embed=embed)

# Replace with your actual bot token from Discord Developer Portal
bot.run('MTUzMjAzNTAxMzk1OTIyMTMxOA.GPJcQg.NBTcNfycePFubEYYkqPaqZ9L_SQ_2H2Lir6MoQ')