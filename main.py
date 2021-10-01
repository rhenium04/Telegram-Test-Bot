try:
    # импорты
    from colorama import init
    from colorama import Fore, Back, Style
    from colorama import Fore
    init()
    import discord
    from discord import *
    from discord.ext import commands
    import asyncio
    import time
    import colorama
    init()
except:
    os.system("pip install colorama")
    os.system("pip install discord")
    os.system("pip install asyncio")

botnamen = 'MF Bot'
admins = set()
print(Fore.RED)
prefix = '*'
print(Fore.BLUE)
token = 'ODkzMzcyMzAxMDUwMDE5ODUw.YVafyg.LHEgbQtvre29XUQsgNKi0uaGit0'


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'MFBot/*help'))
    print(f'{Fore.BLUE}Бот {botnamen} запущен! Для получения списка команд добавьте бота на сервер и пропишите {prefix}help')
@client.event
async def on_guild_join(guild):
  embed = discord.Embed(
        title = 'Привет!',
        description = f'**Я - мультифункциональный бот, который пока умеет не так много, но я активно развиваюсь :)**\nПо всем вопросам писать моему создателю - rhenium#9402.',
        colour = discord.Colour.from_rgb(237, 47, 47)
    )
  await guild.text_channels[0].send(embed = embed)




@client.command()
async def help(ctx, arg=''):
    embed = discord.Embed(
        title = 'Команды',
        description = f'`{prefix}play <название песни>` - играть песню с выбранным названием.\n`{prefix}play <ссылка>` - воспроизведение музыки с YouTube по ссылке\n**Ну а что вы больше ждали от бесплатного непрофессионального бота?**',
          colour = discord.Colour.from_rgb(237, 47, 47)
    )
    await ctx.send(embed = embed)

    
    
    
try:
	client.run(token)
except Exception as e:
	print('Ты указал неверный токен бота или не включил ему интенты!')
	input()
