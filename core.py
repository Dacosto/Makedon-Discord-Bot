
"""
VAZNOVAZNOVAZNOVAZNO:
IMIGRIRANJE NA PYCORD SO SLASH COMMANDS



TODO
V2.0 verzija
dovrsuvanje na komandata !ping  (50%)
dodavanje na MYSQL baza (0%)
dodavanje na User Panel Control (optimalno)
Ureduvanje na kodot (45%)
dodavanje na slash commands ili /  (100%)
dodavanje na poraki vo DM so event (5%)
dodavanje na novi komandi (10%)
hosting(0%)
ban/unban komandi (100%)
kick komanda (100%)

BITNO:
Cogs/kategorii   (5%)
"""

"""
FIXME
podobruvanje malce na komandata !serverpicture
podobruvanje na komandata !avatar




"""

import discord
from discord.ext import commands
from discord import app_commands
from discord import Member


from discord.ext.commands import has_permissions, MissingPermissions



            

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) 




@bot.event
async def on_ready():
    print("Botot e spremen za koristenje")
    try:
      synced = await bot.tree.sync()
      print(f"Sinhronizirano {len(synced)} komandi!")
    except Exception as e:
        print(e)
    
@bot.hybrid_command()
async def pozdrav(ctx):
    await ctx.send(f"Zdravo, {ctx.author.mention}")
    
@bot.tree.command()
async def goodmorning(interaction: discord.Interaction):
    await interaction.response.send_message(f"Dobro utro!, {interaction.author.mention}")
    
@bot.tree.command()
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("Makedon e Makedonski Discord Bot napraven vo Python so pomos na bibliotekata Discord.py Botot e uste vo razvoj, Negovata cel e za koristenje vo PixMap Macedonia,Naskoro ke bidat dodadeni novi informacii.")
   
@bot.tree.command()
async def serverpicture(interaction: discord.Interaction):
    embeded_msg = discord.Embed(title="Slika na Server Iconot", color=discord.Color.red())
    embeded_msg.set_thumbnail(url= interaction.user.avatar)
    embeded_msg.add_field(name="Deskripcija", value=" Slikata ili Icon na serverot!", inline=False)
    embeded_msg.set_image(url= interaction.guild.icon)  
    embeded_msg.set_footer(text=interaction.user, icon_url=interaction.user.avatar)
    await interaction.response.send_message(embed = embeded_msg)
    
@bot.tree.command()
async def avatar(interaction: discord.Interaction):
    embeded_msg = discord.Embed(title="Slika na vasiot avatar!", color=discord.Color.red())
    embeded_msg.set_thumbnail(url= interaction.user.avatar)
    embeded_msg.add_field(name="Deskripcija", value=" Slikata ili Icon na vasiot avatar!", inline=False)
    embeded_msg.set_image(url= interaction.user.avatar)  
    embeded_msg.set_footer(text=interaction.user, icon_url=interaction.user.avatar)
    await interaction.response.send_message(embed = embeded_msg)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(title="Ban", description=f"**{member.mention} e baniran!**",
                              color=discord.Color.green())
        embed.set_footer(text=f'Komandata e iskoristena od - {ctx.author}')
        await member.ban(reason=reason)
        await ctx.send(embed=embed)


bot.tree.command(name="ban", description="komanda za baniranje")


bot.run("HERE U POST YOUR BOT TOKEN")
