import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

from datetime import datetime, timezone

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')	


@client.event
async def on_member_join(member):
	channel = member.server.get_channel("555479219686080534")
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0x7ED060)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_author(name="Member Joined", icon_url=member.avatar_url)
	txt = member.id
	xd = " | Joined: "
	hoho = member.joined_at.__format__('%d. %B %Y %H:%M:%S')
	embed.set_footer(text="ID: "+txt +xd +hoho)
	await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
	channel = member.server.get_channel("555479219686080534")
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0xEA1025)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_author(name="Member Left", icon_url=member.avatar_url)
	xd = member.id
	embed.set_footer(text="ID: "+xd)
	await client.send_message(channel, embed=embed)

@client.event
async def on_message_delete(message):
	channel = client.get_channel('555479219686080534')
	idk = message.content
	eh = "\n"
	embed = discord.Embed(title="", description="Message sent by {0} deleted in {1}".format(message.author.mention, message.channel.mention +eh +idk), color=0xEA1025)
	embed.set_author(name=message.author, icon_url=message.author.avatar_url)
	txt = message.author.id
	xd = " | Message ID: "
	huh = message.id
	embed.set_footer(text="User ID: "+txt +xd +huh)
	await client.send_message(channel, embed=embed)

@client.event
async def on_message_edit(before, after):
	channel = client.get_channel('555479219686080534')
	idk = before.content
	eh = after.content
	embed = discord.Embed(title="", description="Message edited by {0} in {1}".format(before.author.mention, before.channel.mention), color=0x6A7A94)
	embed.add_field(name="Before", value=idk, inline=False)
	embed.add_field(name="After", value=eh, inline=False)
	embed.set_author(name=before.author, icon_url=before.author.avatar_url)
	embed.set_thumbnail(url=before.author.avatar_url)
	txt = before.author.id
	xd = " | Message ID: "
	huh = before.id
	embed.set_footer(text="User ID: "+txt +xd +huh)
	await client.send_message(channel, embed=embed)

@client.event
async def on_channel_create(channel):
	channell = client.get_channel('555479219686080534')
	hi = channel.name
	embed = discord.Embed(title="", description="", color=0x7ED060)
	embed.add_field(name="Channel Created:", value=hi)
	embed.set_author(name=channel.server.name, icon_url=channel.server.icon_url)
	huh = channel.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_channel_delete(channel):
	channell = client.get_channel('555479219686080534')
	hi = channel.name
	embed = discord.Embed(title="", description="", color=0xEA1025)
	embed.add_field(name="Channel Deleted:", value=hi)
	embed.set_author(name=channel.server.name, icon_url=channel.server.icon_url)
	huh = channel.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_channel_update(before, after):
	channell = client.get_channel('555479219686080534')
	idk = before.name
	xd = after.name
	idk1 = before.topic
	xd1 = after.topic
	embed = discord.Embed(title="", description="", color=0x6A7A94)
	embed.add_field(name="Name Before", value=idk, inline=False)
	embed.add_field(name="Name After", value=xd, inline=False)
	embed.add_field(name="Topic Before", value=idk1, inline=False)
	embed.add_field(name="Topic After", value=xd1, inline=False)
	embed.set_author(name=before.server.name, icon_url=before.server.icon_url)
	huh = before.id
	embed.set_footer(text="Channel ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_server_role_create(role):
	channell = client.get_channel('555479219686080534')
	idk = role.name
	embed = discord.Embed(title="Role Created", description=idk, color=0x7ED060)
	embed.set_author(name=role.server.name, icon_url=role.server.icon_url)
	huh = role.id
	embed.set_footer(text="Role ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_server_role_delete(role):
	channell = client.get_channel('555479219686080534')
	idk = role.name
	embed = discord.Embed(title="Role Deleted", description=idk, color=0xEA1025)
	embed.set_author(name=role.server.name, icon_url=role.server.icon_url)
	huh = role.id
	embed.set_footer(text="Role ID: "+huh)
	await client.send_message(channell, embed=embed)

@client.event
async def on_member_ban(member):
	channell = client.get_channel('555479219686080534')
	embed = discord.Embed(title="", description="{0} {1}".format(member.mention, member), color=0xEA1025)
	embed.set_author(name="Member Banned", icon_url=member.avatar_url)
	embed.set_thumbnail(url=member.avatar_url)
	lol = member.id
	embed.set_footer(text="ID: " +lol)
	await client.send_message(channell, embed=embed)

@client.event
async def on_member_unban(server, user):
	channell = client.get_channel('555479219686080534')
	embed = discord.Embed(title="", description="{0} {1}".format(user.mention, user), color=0x337FD5)
	embed.set_author(name="Member Unbanned", icon_url=user.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	lol = user.id
	embed.set_footer(text="ID: " +lol)
	await client.send_message(channell, embed=embed)
  
client.run(str(os.environ.get('BOT_TOKEN')))
