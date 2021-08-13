
import discord
from discord.ext import commands
import time
import os

#UI
user_bot = "Spark#4883"
creator = "Spark © OVERClock - 2021"
version = "version : 1.0.0"
print("Spark#4883 " + version + " © OVERClock")

#DATA
token = os.environ["DISCORD_TOKEN"]
messageid = 819197089778892810
selected_prefix = "!"
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=selected_prefix, intents=intents)
client.remove_command("help") #Delete la commande help prebuild car elle nous empeche d'utiliser la notre


#Début des events


@client.event
async def on_ready():
    nb_servers = str(len(client.guilds))
    if int(nb_servers) == 1:
        await client.change_presence(activity = discord.Game(name = selected_prefix + "help | 1 server"))
    else:
        await client.change_presence(activity = discord.Game(name = selected_prefix + "help | " + nb_servers +" servers"))

@client.event
async def on_member_join(member):
    role1 = discord.utils.get(member.guild.roles, name="Invités")
    role2 = discord.utils.get(member.guild.roles, name="─────────────────────")
    await member.add_roles(role1, role2)
    channel = discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="général")
    await channel.send("Bienvenue <@" + str(member.id) + "> ! :wave:")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="général")
    await channel.send("<@" + str(member.id) + "> a quitté le serveur :wave:")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
    if message_id == messageid:
        if payload.emoji.name == "overwatch":
            role = discord.utils.get(guild.roles, name="Overwatch")
            await member.add_roles(role)
        if payload.emoji.name == "hots":
            role = discord.utils.get(guild.roles, name="Hots")
            await member.add_roles(role)
        if payload.emoji.name == "newworld":
            role = discord.utils.get(guild.roles, name="New World")
            await member.add_roles(role)
        if payload.emoji.name == "apex":
            role = discord.utils.get(guild.roles, name="Apex")
            await member.add_roles(role)
        if payload.emoji.name == "destiny2":
            role = discord.utils.get(guild.roles, name="Destiny 2")
            await member.add_roles(role)
        if payload.emoji.name == "monsterhunter":
            role = discord.utils.get(guild.roles, name="Monster Hunter")
            await member.add_roles(role)
        if payload.emoji.name == "aoe":
            role = discord.utils.get(guild.roles, name="AoE")
            await member.add_roles(role)
        if payload.emoji.name == "minecraft":
            role = discord.utils.get(guild.roles, name="Minecraft")
            await member.add_roles(role)
        if payload.emoji.name == "jeuxdivers":
            role = discord.utils.get(guild.roles, name="Jeux divers")
            await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)
    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
    if message_id == messageid:
        if payload.emoji.name == "overwatch":
            role = discord.utils.get(guild.roles, name="Overwatch")
            await member.remove_roles(role)
        if payload.emoji.name == "hots":
            role = discord.utils.get(guild.roles, name="Hots")
            await member.remove_roles(role)
        if payload.emoji.name == "newworld":
            role = discord.utils.get(guild.roles, name="New World")
            await member.remove_roles(role)
        if payload.emoji.name == "apex":
            role = discord.utils.get(guild.roles, name="Apex")
            await member.remove_roles(role)
        if payload.emoji.name == "destiny2":
            role = discord.utils.get(guild.roles, name="Destiny 2")
            await member.remove_roles(role)
        if payload.emoji.name == "monsterhunter":
            role = discord.utils.get(guild.roles, name="Monster Hunter")
            await member.remove_roles(role)
        if payload.emoji.name == "aoe":
            role = discord.utils.get(guild.roles, name="AoE")
            await member.remove_roles(role)
        if payload.emoji.name == "minecraft":
            role = discord.utils.get(guild.roles, name="Minecraft")
            await member.remove_roles(role)
        if payload.emoji.name == "jeuxdivers":
            role = discord.utils.get(guild.roles, name="Jeux divers")
            await member.remove_roles(role)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content == "Hello":
        await message.channel.send("Hi !")
    await client.process_commands(message)


#Fin des events

#Début des commandes


@client.command()
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send("Test ok")
    time.sleep(1)
    await ctx.channel.purge(limit=1)

@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    em = discord.Embed(title="Spark", description=":gear: Liste des commandes :", colour=0x000000)
    em.add_field(name="`" + selected_prefix + "clear x`", value="Nettoie les x derniers messages du salon", inline=False)
    em.add_field(name="`" + selected_prefix + "game`", value="Change l'activité du bot", inline=False)
    em.add_field(name="`" + selected_prefix + "regles`", value="Les règles qui régissent ce serveur", inline=False)
    em.add_field(name="`" + selected_prefix + "restart`", value="Redémarre le bot", inline=False)
    em.add_field(name="`" + selected_prefix + "test`", value="Commande test", inline=False)
    em.add_field(name="`" + selected_prefix + "ver`", value="Affiche la version du bot", inline=False)
    em.set_footer(text = creator, icon_url=client.user.avatar_url)
    await ctx.channel.send(embed=em)

@client.command()
async def prefix(ctx, arg):
    client.command_prefix = arg
    await ctx.channel.send("**Préfixe changé avec succès !** :sparkles:")

@client.command()
async def regles(ctx):
    await ctx.channel.purge(limit=1)
    em = discord.Embed(title = ":page_with_curl: Règles", colour=0x000000)
    em.set_author(name = ctx.guild.name, icon_url=ctx.guild.icon_url)
    em.add_field(name = "Voici les règles qui régissent ce serveur :", value =
        """
        → Pas de racisme ou toute autre forme de discrimination du genre.
        → Pas de flood/spam/pollution des différents salons.
        → Pas d'avatars/pseudos choquants/encombrants. Les administrateurs se réservent le droit de changer votre pseudo s'il ne respecte pas ces règles. 
        → Les administrateurs se réservent également le droit de Mute/Kick/Ban les personnes ne respectant pas les règles et cherchant à nuire à autrui/l’ambiance du Discord.
        """, inline=True)
    em.set_footer(text = creator, icon_url = client.user.avatar_url)
    await ctx.channel.send(embed=em)

@client.command()
async def clear(ctx, arg):
    await ctx.channel.purge(limit = int(arg)+1)
    if int(arg) == 1:
        await ctx.channel.send(":recycle: **1 message nettoyé !**")
    else:
        await ctx.channel.send(":recycle: **" + str(int(arg)) + " messages nettoyés !**")
    time.sleep(1)
    await ctx.channel.purge(limit=1)

@client.command()
async def game(ctx, arg):
    await ctx.channel.purge(limit=1)
    await client.change_presence(activity = discord.Game(name=arg))
    await ctx.channel.send("Joue maintenant à **" + arg + "** !")
    time.sleep(2)
    await ctx.channel.purge(limit=1)

@client.command()
async def ver(ctx):
    await ctx.channel.purge(limit=1)
    em = discord.Embed(title = selected_prefix + "help pour commencer", description = version + " ", colour=0x000000)
    em.set_footer(text = creator, icon_url=client.user.avatar_url)
    await ctx.channel.send(embed=em)

@client.command()
async def addrole(ctx, arg1, arg2):
    member = ctx.guild.get_member_named(arg1)
    role = discord.utils.get(ctx.guild.roles, name=arg2)
    await member.add_roles(role)
    await ctx.channel.send("**Rôle ajouté avec succès !** :sparkles:")
    await ctx.channel.purge(limit=1)

@client.command()
async def create_role_embed(ctx):
    await ctx.channel.purge(limit=1)
    overwatch = discord.utils.get(ctx.message.guild.emojis, name="overwatch")
    hots = discord.utils.get(ctx.message.guild.emojis, name="hots")
    newworld = discord.utils.get(ctx.message.guild.emojis, name="newworld")
    apex = discord.utils.get(ctx.message.guild.emojis, name="apex")
    destiny2 = discord.utils.get(ctx.message.guild.emojis, name="destiny2")
    monsterhunter = discord.utils.get(ctx.message.guild.emojis, name="monsterhunter")
    aoe = discord.utils.get(ctx.message.guild.emojis, name="aoe")
    minecraft = discord.utils.get(ctx.message.guild.emojis, name="minecraft")
    jeuxdivers = discord.utils.get(ctx.message.guild.emojis, name="jeuxdivers")
    em = discord.Embed(title = ":page_with_curl: Roles", colour=0x000000)
    em.set_author(name = ctx.guild.name, icon_url=ctx.guild.icon_url)
    em.add_field(name = "Si vous possédez déjà un rôle, il est inutile de remettre une réaction !", value =
        f"""
        {overwatch} Overwatch
        {hots} Hots
        {newworld} New World
        {apex} Apex Legends
        {destiny2} Destiny 2
        {monsterhunter} Monster Hunter
        {aoe} Age of Empires
        {minecraft} Minecraft
        {jeuxdivers} Jeux divers
        """, inline=True)
    em.set_footer(text = creator, icon_url = client.user.avatar_url)
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction(overwatch)
    await msg.add_reaction(hots)
    await msg.add_reaction(newworld)
    await msg.add_reaction(apex)
    await msg.add_reaction(destiny2)
    await msg.add_reaction(monsterhunter)
    await msg.add_reaction(aoe)
    await msg.add_reaction(minecraft)
    await msg.add_reaction(jeuxdivers)

@client.command()
async def restart(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(":wave: **A plus !**")
    time.sleep(1)
    await ctx.channel.purge(limit=1)
    await client.close()


#Fin des commandes

client.run(token)
