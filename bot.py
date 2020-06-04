import discord
import random
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='!') # Префикс комманд (!test)
token = "" # Секрет приложения
words = "../towns_game_twitch/towns.txt" # Файл с городами


# Переменные для функционирования бота (не трогать!)
city = ""
gameisstart = False
cities = list()
verb = "" 


# Эвент нового сообщения
@bot.command(pass_context=True)
async def tn(ctx, town):

	nick = ctx.author.name
	global city
	global gameisstart
	global verb

	if not (len(town.split(" ")) == 1 and gameisstart):
		return


	message = town.lower()
	if message in cities:
		await ctx.channel.send(nick + ", the city has already been named")
	elif message[0].strip() == verb:
		list_city = open(words, "r", encoding="UTF-8").readlines()
		if not message.capitalize().strip() in "".join(list_city).split("\n"):
			await ctx.channel.send(nick + ", this city is not in the dictionary")
			print("Нету в словаре: " + message)
			return

		city = message
		city = city.capitalize()

		cities.append(city.lower().strip())
		
		verb = city[-2] if city[-1] == "ь" else city[-1]
		
		await ctx.channel.send("City " + city + " was named " + nick + " next city letter '" + verb + "'")
	else:
		await ctx.channel.send(nick + ", letter city '" + verb + "'")

	time.sleep(5)

# Эвент команд
@bot.command()
async def stg(ctx):

	global gameisstart
	global city
	global cities
	global verb

	cities = list()
	gameisstart = True
	list_city = open(words, "r", encoding="UTF-8").readlines()
	city = list_city[random.randint(0, len(list_city)-1)]
	cities.append(city.lower())

	verb = city[-3] if city[-2] == "ь" else city[-2]
	
	await ctx.channel.send("Game 'Cities' started(=Кузнецк), first city - " + city)

	time.sleep(5)


@bot.command()
async def voice(ctx):
	await ctx.author.voice.channel.connect()


print("Бот запущен")
bot.run(token)
