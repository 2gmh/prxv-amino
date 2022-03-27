from edamino import Context, logger, Client, api, Bot
from edamino.objects import UserProfile, SocketAnswer, Message
from edamino.api import Embed,MessageType
from asyncio import sleep
import re 
import time
import random

bot = Bot('correo', 'passwd', 'prefix')

@bot.event()
async def on_ready(profile: UserProfile):
    logger.info(f'{profile.nickname} ha sido encendido')
  

@bot.command('ping')
async def on_piing(ctx: Context):
    await ctx.reply("Pong!")

@bot.command('embed')
async def on_embed(ctx: Context):
    embed = Embed(
        title=ctx.msg.author.nickname,
        object_type=0,
        object_id=ctx.msg.author.uid,
        content="Hola."
    )
    await ctx.send("uwu", embed=embed)

@bot.command('join')
async def on_join_community(ctx: Context):
    msg = ctx.msg.content
    comu = re.search("http://aminoapps.com/c/", msg)
    cmd = ' '.join(ctx.msg.content.split()[1:])

    if comu:
        ide = await ctx.get_info_link(cmd)
        idlink = ide.community.ndcId
        with ctx.set_ndc(idlink):
            await ctx.join_community()
        await ctx.reply('Me he unido.')

@bot.command('rnd')
async def on_biba(ctx: Context):
    async with ctx.typing():
        await ctx.reply(f'{random.randint(1, 10000)}')

·
@bot.command('spd')
async def on_speed(ctx: Context):
    timestamp = time.time()
    await ctx.reply(f' {time.time() - timestamp:.2f}s.')

@bot.command('start')
async def on_check(ctx: Context):
    await ctx.join_thread(1)
    await ctx.join_channel(5)

    image = await ctx.download_from_link(
        'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Gull_portrait_ca_usa.jpg/1280px-Gull_portrait_ca_usa.jpg'
    )


@bot.command('typing')
async def on_typing(ctx: Context):
    async with ctx.typing():
        await sleep(3)
        await ctx.reply('✔')


@bot.command(['rec', 'recording'])
async def on_ping(ctx: Context):
    async with ctx.recording():
        await sleep(3)
        await ctx.reply('🎁')

@bot.command('echo')
async def echo(ctx: Context, args: str):
    await ctx.reply(args)

@bot.event([MessageType.GROUP_MEMBER_JOIN])
async def on_member_join(ctx: Context):
    embed = Embed(
        title=ctx.msg.author.nickname, 
        object_type=0, 
        object_id=ctx.msg.author.uid,
        content="lalala"
    )
    await ctx.send("Welcome to the chat!", embed=embed)

@bot.command('in')
async def ins(ctx: Context):
    await ctx.reply(f"{random.choice(response3)}")

response3 =['No',
   'Pelotudito',
   'Down del orto',
   'Virgo',
   'Anda a comer pija',
   'Gil',
   'Hijo de puta',
   'Cerra el orto un rato',
   'Matate maricon',
   'Chupala hdp',
   'Maldito hijo de puta',
   'NO LO SOÑEEEE',
   'Puta',
   'sucia', 
   'wanquera',
   'culo roto',
   'cabeza de pingo',
   'forra',
   'negra olor a mandarina', 'pelotuda', 
   'cajetuda',
   'hija de puta',
   'hija de re mil puta',
   'hija de una huracanada de putas',
   'hija de una camionada de re mil putas',
   'adicta al chino tuerto, negra chota', 
   'mal nacida', 'culeada',
   'mal culeada',
   'puta barata', 
   'tira goma',
   'cara de pingo', 
   'cara de concha', 
   'cara de culo',
   'olor a culo',
   'negra lechera',
   'petera', 
   'puta del orto',
   'wanaca',
   'olor a orto',
   'verdulera', 
   'olor a pedo',
   'traga forros', 
   'marica', 
   'culo descocido',
   'traga pingo', 
   'traga sable', 
   'traga chota', 
   'poronga arenosa',
   'zorra, zorrita', 'ura', 
   'urita',
   'traidora', 
   'tarada', 
   'boba', 
   'turrita', 
   'trolita',
   'gnomo de jardin',
   'tarzan de macetas',
   'rompe pija',
   'lagarto',
   'mono de mierda',
   'jorobado inutil',
   'chupa culos']

@bot.command('chiste')
async def on_typing(ctx: Context):
    async with ctx.typing():
        await sleep(3)
        await ctx.reply('Porque jesus no corta con su novia?')
        await sleep(3)
        await ctx.reply('Porque esta bien clavado')


@bot.event()
async def on_mention(ctx: Context):
  await ctx.reply(f'<$@{ctx.msg.author.nickname}$>', mentions=[ctx.msg.uid])

@bot.command('image')
async def on_image(ctx: Context):
  
    image = await ctx.download_from_link(f"{random.choice(imagenes)}")
    await ctx.send_image(image)

imagenes = ['https://i.pinimg.com/originals/1a/e5/98/1ae598b32f93b8de53319c621ec0e07e.jpg',
'https://i.pinimg.com/564x/ea/ab/f4/eaabf41de66ab7f96c034640f23294b1.jpg',
]

@bot.command('by')
async def baby(ctx: Context):
    image = await ctx.download_from_link('https://i.pinimg.com/564x/ea/ab/f4/eaabf41de66ab7f96c034640f23294b1.jpg')
    await ctx.reply("Hey baby")
    await ctx.send_image(image)

@bot.command('gif')
async def on_gif(ctx: Context):
    gif = await ctx.download_from_link('https://i.pinimg.com/originals/d1/f2/6c/d1f26c4cc48446457e6d757093d8a680.gif')
    await ctx.send_gif(gif)

@bot.command(['play', 'p'])
async def on_example(ctx: Context):
    await ctx.reply('Good! 🎉')
  
bot.start()
