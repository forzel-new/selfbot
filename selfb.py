# -*- coding: utf-8 -*-

logo = """

####### #######  #####                       ######               
#            #  #     # ###### #      ###### #     #  ####  ##### 
#           #   #       #      #      #      #     # #    #   #   
#####      #     #####  #####  #      #####  ######  #    #   #   
#         #           # #      #      #      #     # #    #   #   
#        #      #     # #      #      #      #     # #    #   #   
#       #######  #####  ###### ###### #      ######   ####    #    """
print(logo)

prefix = input(f'\nПрефикс --> ')

import asyncio
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice
# импортируем важные библы
crashed = []
v = '1.0.0'

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True)
# создаем переменную бота
client.remove_command('help')

global spam
spam = True

@client.event
async def on_ready():
	print(f'\n[ FZSelfBot ] Аккаунт загружен | Работаю на клиенте {client.user}')
	print(f'[ FZSelfBot ] Для просмотра списка команд введите {prefix}help')

@client.command()
async def help(ctx):
	embed = discord.Embed(
		title = f'FZSelfBot {v} | GitHub Version',
		description = f'`{prefix}getlink` - выдаст ссылку на скачивание файлов селф-бота\n`{prefix}say [ текст ]` - отправить сообщение в эмбеде\n`{prefix}echo [ текст ]` - отправить сообщение в эмбеде с рандомным цветом\n`{prefix}ping` - проверить пинг селф-бота\n`{prefix}create_guild [ имя ]` - создать сервер и удалить на нём все каналы\n`{prefix}crash` - авто краш сервера\n`{prefix}delguild` - удалить текущий сервер (если есть права)\n`{prefix}spam [ Текст ]` - бесконечный спам вашим текстом\n`{prefix}stop` - остановить спам\n`{prefix}spamv2 [ кол-во сообщений ] [ текст ]` - спам текстом в обход 90% анти-спам систем\n`{prefix}killchat [ кол-во сообщений ]` - засорить чат, так что будет просто черный экран\n`{prefix}autoraid` - автоматический рейд сервера\n`{prefix}status [ тип статуса ] [ текст ]` - установить статус\n`{prefix}hack` - клонирование текущего сервера\n`{prefix}popit` - отправить поп ит в чат\n`{prefix}ball [ вопрос ]` - задать вопрос магическому шару',
		colour = discord.Colour.from_rgb(111,228,55)
	)
	embed.set_footer(text=f'FZSelfBot {v}', icon_url='https://yt3.ggpht.com/0x2AH-dWTYTfIyuiMTWcDFgBOTRjfZZx0cdEf0xRTEer9xmFJS53zXgHH86V6UPh2r9gYjGQC4k=s88-c-k-c0x00ffffff-no-rj')
	await ctx.send(embed=embed)

@client.command()
async def getlink(ctx):
	embed = discord.Embed(
		title = f'FZSelfBot {v}',
		description = f'Вы используете селф-бота `FZSelfBot` версии `{v}`\nИсходный код: :earth_asia: [GitHub](https://github.com/forzel-new/selfbot)',
		colour = discord.Colour.from_rgb(randint(0,255), randint(0,255), randint(0,255))
	)
	await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, text=''):
	if text == '':
		msg = await ctx.send(f'Укажите текст!')
		time.sleep(1)
		await msg.delete()
		await ctx.message.delete()
	else:
		await ctx.message.delete()
		await ctx.send(embed=discord.Embed(description=text))

@client.command()
async def echo(ctx, *, text=''):
	if text == '':
		msg = await ctx.send(f'Укажите текст!')
		time.sleep(1)
		await msg.delete()
		await ctx.message.delete()
	else:
		await ctx.message.delete()
		await ctx.send(embed=discord.Embed(description=text, colour=discord.Colour.from_rgb(randint(0,255), randint(0,255), randint(0,255))))

@client.command()
async def ping(ctx):
	await ctx.send(embed=discord.Embed(title=f':ping_pong: Понг!', description = f'Задержка API - {round(client.latency * 1000)}ms', colour=discord.Colour.from_rgb(111,228,111)))

@client.command()
async def create_guild(ctx, *, nameg='fzselfbot guild'):
	new = await client.create_guild(name=nameg)
	listc = await new.fetch_channels()
	for c in listc:
		await c.delete()

	await new.create_text_channel('made-by-fzselfbot')

	embed = discord.Embed(
		title = 'Готово :white_check_mark:',
		description = f'Был создан сервер {nameg}',
		colour = discord.Colour.from_rgb(randint(0,255), randint(0,255), randint(0,255))
	)
	await ctx.send(embed=embed)

@client.command()
async def crash(ctx):
	await ctx.guild.edit(name='Crashed by FZSelfBot')
	for r in ctx.guild.roles:
		try:
			await r.delete()
		except:
			pass


	for c in ctx.guild.channels:
		try:
			await c.delete()
		except:
			pass

	for i in range(50):
		await ctx.guild.create_role(name='Crash By FZSelfBot')
		ch = await ctx.guild.create_text_channel('crash-by-fzselfbot')
		await ch.create_webhook(name='crash4d')

@client.event
async def on_guild_channel_create(channel):
	if channel.name == 'crash-by-fzselfbot':
		for i in range(100):
			hooks = await channel.webhooks()
			for hook in hooks:
				await hook.send('@everyone @here Данный сервер крашится селф-ботом fzselfbot')


@client.command()
async def delguild(ctx):
	try:
		await ctx.guild.delete()
	except Exception as e:
		embed = discord.Embed(
			title = 'Ошибка :x:',
			description = f'Произошла ошибка при удалении сервера | `{e}`',
			colour = discord.Colour.from_rgb(133,228,61)
		)
		await ctx.send(embed=embed)

@client.command()
async def spam(ctx, *, text=None):
	embederr = discord.Embed(
		title = 'Ошибка :x:',
		description = 'Укажите текст спама!',
		colour = discord.Colour.from_rgb(228,0,111)
	)
	embed = discord.Embed(
		title = 'Успешно :white_check_mark:',
		description = f'Спам запущен! Для остановки напишите {prefix}stop',
		colour = discord.Colour.from_rgb(228,0,111)
	)
	if text == None:
		await ctx.send(embed=embederr)
	else:
		global spam
		spam = True
		while spam:
			await ctx.send(text)

@client.command()
async def stop(ctx):
	global spam
	spam = False
	await ctx.message.add_reaction('✅')

@client.command()
async def spamv2(ctx, num=0, *, text=''):
	if num == 0 or text in ['']:
		await ctx.send(f'Правильное использование команды: `{prefix}spamv2 [ кол-во сообщений ] [ текст ]`')
	else:
		for spam in range(int(num)):
			await ctx.send(f'{text}\n||{randint(0,1000000000)}||')

@client.command()
async def killchat(ctx, count=5):
	for i in range(int(count)):
		text = f'||{randint(0,1918177181)}|| die...:hot_face: :hot_face: \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndie...:hot_face: :hot_face:'
		await ctx.send(text)
	await ctx.message.delete()

async def sendhook(ctx, channelm):
		for i in range(100):
			hooks = await channelm.webhooks()
			for hook in hooks:
				await hook.send('@everyone @here raid by fzselfbot!')

@client.command()
async def autoraid(ctx):
	await ctx.message.delete()
	for i in range(6):
		text = f'{randint(0,999)} | Raid by FZSelfBot! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||'
		await ctx.send(text)
	for c in ctx.guild.text_channels:
		try:
			await c.create_webhook(name='Raid By FZSelfBot')
		except Exception as e:
			print(e)

	try:
			for c in ctx.guild.text_channels:
				asyncio.create_task(sendhook(ctx, channelm=c))
				hooks = await c.webhooks()
				for hook in hooks:
					await hook.send(f'{randint(0,999)} | Raid by FZSelfBot! @everyone @here')
	except Exception as e:
			print(e)

	for c in ctx.guild.text_channels:
		try:
			await c.send(f'{randint(0,999)} | Raid by FZSelfBot! @everyone @here\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n||{randint(0,1338)}||')
		except:
			pass

@client.command()
async def status(ctx, arg='', *, names=''):
    bll = [''] # не смейтесь ебать, просто not == '' не работало, а искать решение лень
    if arg == 'stream' and names not in bll:
        await client.change_presence(activity=discord.Streaming(name=names, url='https://twitch.tv/404'))
        await ctx.message.add_reaction('✅')
    elif arg == 'watch' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'listen' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'play' and names not in bll:
        await client.change_presence(activity=discord.Game(name=names))
        await ctx.message.add_reaction('✅')
    else:
        embed = discord.Embed(
            title = 'Аргументы',
            description = f'`stream` - стрим статус\n`watch` - статус смотрит\n`listen` - статус слушает\n`play` - статус играет',
            colour = discord.Colour.from_rgb(29, 224, 11)
        )
        await ctx.send(embed=embed)

class console():
	def log(text):
		print(f'[{time.strftime("%H:%M:%S")}] {text}')
	def debug(text):
		print(f'[{time.strftime("%H:%M:%S")}] [ОТЛАДКА] {text}')


#cтарый код матвея, досихпор работает
@client.command()
async def hack(ctx):
	if not ctx.guild: return
	timel = time.time()
	guild = ctx.guild
	msglog=ctx.message
	console.log(f'Начинаю клонирование сервера {guild.name}...')
	await msglog.delete()
	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | ⏳',
					description = 'Сервер создан - :x:\nСозданы роли - :x:\nСозданы каналы - :x:\nНастроены права каналов - :x:\nСозданы эмодзи - :x:',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)

	msgs = await ctx.send(embed=embed)
	icon_hash = guild.icon
	with open('clone_icon.png', 'wb+') as handle:
		handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
	new_guild = await client.create_guild(name=guild.name, icon=open('clone_icon.png', 'rb').read())
	for channel in new_guild.channels:
		try:
			await chennel.delete()
		except:
			pass

	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | ⏳',
					description = 'Сервер создан - :white_check_mark:\nИдёт создание ролей, пожалуйста, подождите... - ⏳\nСозданы каналы - :x:\nНастроены права каналов - :x:\nСозданы эмодзи - :x:',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)
	await msgs.edit(embed=embed)

	console.log(f'Создан сервер с именем {guild.name} с нужной иконкой, начинаю создание ролей')
	roles = {}
	r = guild.roles
	r.reverse()
	for role in r:
		if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
		new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
		roles[role] = new_role
	everyone = guild.default_role
	roles[everyone] = new_guild.default_role
	await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)

	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | ⏳',
					description = 'Сервер создан - :white_check_mark:\nСозданы роли - :white_check_mark:\nИдёт создание каналов, пожалуйста, подождите... - ⏳\nНастроены права каналов - :x:\nСозданы эмодзи - :x:',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)
	await msgs.edit(embed=embed)

	console.log(f'Создание ролей завершено, начинаю создание каналов')
	for dc in await new_guild.fetch_channels():
		await dc.delete()
	channels = {None: None}
	for cat in guild.categories:
		new_c = await new_guild.create_category(name=cat.name, position=cat.position)
		channels[cat] = new_c
	for catt in guild.by_category():
		cat = catt[0]
		chs = catt[1]
		if cat != None:
			for c in chs:
				if c.type==discord.ChannelType.text:
					new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				elif c.type==discord.ChannelType.voice:
					new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
				elif c.type==discord.ChannelType.news:
					new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				channels[c] = new_c
		else:
			for c in chs:
				if c.type==discord.ChannelType.text:
					new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				elif c.type==discord.ChannelType.voice:
					new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
				elif c.type==discord.ChannelType.news:
					new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
				channels[c] = new_c
	console.log(f'Создание каналов завершено, начинаю настройку оверврайтов')
	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | ⏳',
					description = 'Сервер создан - :white_check_mark:\nСозданы роли - :white_check_mark:\nСозданы каналы - :white_check_mark:\nИдёт настройка прав каналов, пожалуйста, подождите... - ⏳\nСозданы эмодзи - :x:',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)
	await msgs.edit(embed=embed)
	for c in guild.channels:
		overs = c.overwrites
		over_new = {}
		for target,over in overs.items():
			if isinstance(target, discord.Role):
				try:
					over_new[roles[target]] = over
				except:
					pass
			else:
				console.debug(f'(OVERWRITES) Пропускаю {target.name}, так как это юзер')
		await channels[c].edit(overwrites=over_new)
	await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
	console.log(f'Настройка оверврайтов завершена, начинаю создание эмодзи...')
	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | ⏳',
					description = 'Сервер создан - :white_check_mark:\nСозданы роли - :white_check_mark:\nСозданы каналы - :white_check_mark:\nНастроены права каналов - :white_check_mark:\nИдёт создание эмодзи, пожалуйста, подождите... - ⏳',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)
	await msgs.edit(embed=embed)
	countem = 0
	for emoji in guild.emojis:
		try:
			if int(countem) == 50:
				break
			else:
				url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
				await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
				countem +=1
		except:
			print('не могу скопировать эмодзю')
			break
	os.remove('clone_icon.png')
	times = int(time.time() - timel)
	console.log(f'Завершено клонирование сервера. Операция заняла {times} сек.')
	embed = discord.Embed(
					title = f'Клонирование сервера {ctx.guild.name} | Готово :white_check_mark:',
					description = f'Сервер создан - :white_check_mark:\nСозданы роли - :white_check_mark:\nСозданы каналы - :white_check_mark:\nНастроены права каналов - :white_check_mark:\nСозданы эмодзи - :white_check_mark:\n\nОперация заняла {times} секунд',
					colour = discord.Colour.from_rgb(237, 47, 47)
	)
	await msgs.edit(embed=embed)

@client.command()
async def popit(ctx):
	embed = discord.Embed(
		title = 'Поп-ит',
		description = f'||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:|| ||:white_large_square:||\n||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:||\n||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:||\n||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:||\n||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:|| ||:yellow_square:||',
		colour = discord.Colour.from_rgb(228,100,16)
	)
	embed.set_footer(text=f'По запросу {ctx.author}')
	msgg = await ctx.send(embed=embed)

@client.command()
async def ball(ctx, *, question):
	answers = ['Конечно же да :ok_hand:', 'Я считаю, что нет :x:', 'Весьма сомнительно, но правда :astonished:', 'Конечно же нет! :poop:', 'Шар не знает что на это ответить :robot:', 'Очень крутой вопрос, я его не понял :grin:']
	answer = random.choice(answers)
	embed = discord.Embed(
		title = 'Шар думает... :timer:',
		description = f'Я думаю, что ответить на `{question}`...',
		colour = discord.Colour.from_rgb(0,228,66)
	)
	msg = await ctx.send(embed=embed)
	time.sleep(1.5)
	embed = discord.Embed(
		title = 'Шар ответил на ваш вопрос :magic_wand:',
		description = f'Ответ: {answer}',
		colour = discord.Colour.from_rgb(0,228,66)
	)
	await msg.edit(embed=embed)

with open('token.txt', 'r') as f:
	tkn = f.read()
client.run(tkn, bot=False)