import discord
from discord.ext import commands
from utils import *
from my_token import MY_TOKEN


hero_desc = '!hero - генерация рандомного героя с рандомным билдом'
build_desc = ('!build - генерация билда для указанного после команды героя. '  
	'Героя писать на английском, хотя бы первые 5 букв. некоторые общепринятые сокращиения принимаются. '
	'(Например для билда на Келтузада можно ввести "kelthuzad" или "Kel" или "ktz") '
	'Например(билд на самуро): !build sam')
role_desc = ('!role - генерация героя с указанной ролью(ролями) после команды. '
	'Роли указываются одной буквой через запятую: t - tank, b - bruiser, m - melee, r - ranged, h - heal, s - support. '
	'Например(сгенерить рендж дд или хила): !role r,h')


with open('heroes.json', 'r', encoding="utf-8") as fd:
	data = eval(fd.read())

intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}  ({bot.user.id})')

# @bot.command()
# async def hero(ctx, brief='random hero with random build', descrintion=hero_desc):
# 	output = random_hero(data)
# 	await ctx.send(output)

@bot.command()
async def build(ctx, arg='', brief='build for specific hero', descrintion=build_desc):
	try: 
		output = roled_hero(arg, data)
	except:
		try:
			output = hero_build(arg, data)
		except:
			output = random_hero(data)
	await ctx.send(output)

# @bot.command()
# async def role(ctx, arg, brief='random hero+build of specific role', descrintion=role_desc):
# 	output = roled_hero(arg, data)
# 	await ctx.send(output)

bot.run(MY_TOKEN)	