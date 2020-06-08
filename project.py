# - *- coding:utf- 8 - *-
import requests
import json
import tqdm
import vk
import re
import random
import sys
import socks,socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'ss-03.s5.ynvv.cc',999)
socks.setdefaultproxy(socks.PROXY_TYPE_HTTP,'ss-03.s5.ynvv.cc',999)
socket.socket = socks.socksocket
reload(sys)
sys.setdefaultencoding('utf-8')
token = '41e2cbef8cfe548c73bf85e58b8c1a6ee3552f632a534fb822a8652c139deb4d8913438fef48995b12701'
TOKEN = '41e2cbef8cfe548c73bf85e58b8c1a6ee3552f632a534fb822a8652c139deb4d8913438fef48995b12701'
version = '5.92'
session = vk.Session(access_token=token)
vk_api = vk.API(session)
data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -36018360,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_pop = []
k = 0
while k <= 99:
    music_pop.append(data['response']['items'][k])
    k += 1
music_pop_2 = []
for g in music_pop:
    try:
        music_pop_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_pop_2.append('sos')
    except IndexError:
        music_pop_2.append('sos')
vv = 0
while vv < 20:
    for x in music_pop_2:
        if x == 'sos':
            music_pop_2.remove(x)
    vv += 1
music_pop_artist = []
music_pop_title = []
v = 0
while v < len(music_pop_2):
    music_pop_artist.append(music_pop_2[v]['artist'])
    v += 1
v = 0
while v < len(music_pop_2):
    music_pop_title.append(music_pop_2[v]['title'])
    v += 1
music_pop_end = []
dd = 0
while dd < len(music_pop_title):
    ccc = []
    ccc.append(music_pop_artist[dd])
    ccc.append(music_pop_title[dd])
    music_pop_end.append(ccc)
    dd += 1
russian_pop = []
for h in music_pop_end:
    my_list = [' - '.join(h)]
    russian_pop.append(my_list)


data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -45172096,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_rap = []
k = 0
while k <= 99:
    music_rap.append(data['response']['items'][k])
    k += 1
music_rap_2 = []
for g in music_rap:
    try:
        music_rap_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_rap_2.append('sos')
    except IndexError:
        music_rap_2.append('sos')
vv = 0
while vv < 20:
    for x in music_rap_2:
        if x == 'sos':
            music_rap_2.remove(x)
    vv += 1
music_rap_artist = []
music_rap_title = []
v = 0
while v < len(music_rap_2):
    music_rap_artist.append(music_rap_2[v]['artist'])
    v += 1
v = 0
while v < len(music_rap_2):
    music_rap_title.append(music_rap_2[v]['title'])
    v += 1
music_rap_end = []
dd = 0
while dd < len(music_rap_title):
    ccc = []
    ccc.append(music_rap_artist[dd])
    ccc.append(music_rap_title[dd])
    music_rap_end.append(ccc)
    dd += 1
rap = []
for h in music_rap_end:
    my_list = [' - '.join(h)]
    rap.append(my_list)

data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -189177866,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_italian_rap = []
k = 0
while k <= 70:
    music_italian_rap.append(data['response']['items'][k])
    k += 1
music_italian_rap_2 = []
for g in music_italian_rap:
    try:
        music_italian_rap_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_italian_rap_2.append('sos')
    except IndexError:
        music_italian_rap_2.append('sos')
vv = 0
while vv < 20:
    for x in music_italian_rap_2:
        if x == 'sos':
            music_italian_rap_2.remove(x)
    vv += 1
music_italian_rap_artist = []
music_italian_rap_title = []
v = 0
while v < len(music_italian_rap_2):
    music_italian_rap_artist.append(music_italian_rap_2[v]['artist'])
    v += 1
v = 0
while v < len(music_italian_rap_2):
    music_italian_rap_title.append(music_italian_rap_2[v]['title'])
    v += 1
music_italian_rap_dict = dict(zip(music_italian_rap_artist, music_italian_rap_title))
music_italian_rap_end = []
dd = 0
while dd < len(music_italian_rap_title):
    ccc = []
    ccc.append(music_italian_rap_artist[dd])
    ccc.append(music_italian_rap_title[dd])
    music_italian_rap_end.append(ccc)
    dd += 1
italian_rap = []
for h in music_italian_rap_end:
    my_list = [' - '.join(h)]
    italian_rap.append(my_list)


data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -49290676,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_indie = []
k = 0
while k <= 99:
    music_indie.append(data['response']['items'][k])
    k += 1
music_indie_2 = []
for g in music_indie:
    try:
        music_indie_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_indie_2.append('sos')
    except IndexError:
        music_indie_2.append('sos')
vv = 0
while vv < 20:
    for x in music_indie_2:
        if x == 'sos':
            music_indie_2.remove(x)
    vv += 1
music_indie_artist = []
music_indie_title = []
v = 0
while v < len(music_indie_2):
    music_indie_artist.append(music_indie_2[v]['artist'])
    v += 1
v = 0
while v < len(music_indie_2):
    music_indie_title.append(music_indie_2[v]['title'])
    v += 1
music_indie_dict = dict(zip(music_indie_artist, music_indie_title))
music_indie_end = []
dd = 0
while dd < len(music_indie_title):
    ccc = []
    ccc.append(music_indie_artist[dd])
    ccc.append(music_indie_title[dd])
    music_indie_end.append(ccc)
    dd += 1
indie = []
for h in music_indie_end:
    my_list = [' - '.join(h)]
    indie.append(my_list)

data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -110677273,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_french_rap = []
k = 0
while k <= 99:
    music_french_rap.append(data['response']['items'][k])
    k += 1
music_french_rap_2 = []
for g in music_french_rap:
    try:
        music_french_rap_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_french_rap_2.append('sos')
    except IndexError:
        music_french_rap_2.append('sos')
vv = 0
while vv < 20:
    for x in music_french_rap_2:
        if x == 'sos':
            music_french_rap_2.remove(x)
    vv += 1
music_french_rap_artist = []
music_french_rap_title = []
v = 0
while v < len(music_french_rap_2):
    music_french_rap_artist.append(music_french_rap_2[v]['artist'])
    v += 1
v = 0
while v < len(music_french_rap_2):
    music_french_rap_title.append(music_french_rap_2[v]['title'])
    v += 1
music = []
for k in music_french_rap_title:
    l = k.replace("[OKLM Russie]", '')
    music.append(l)
music_title_norm = []
for i in music:
    v = i.replace("[OKLM Radio]", '')
    music_title_norm.append(v)

music_french_rap_end = []
dd = 0
while dd < len(music_title_norm):
    ccc = []
    ccc.append(music_french_rap_artist[dd])
    ccc.append(music_title_norm[dd])
    music_french_rap_end.append(ccc)
    dd += 1
french_rap = []
for h in music_french_rap_end:
    my_list = [' - '.join(h)]
    french_rap.append(my_list)


data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -7057,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()

music_russian_rap = []
k = 0
while k <= 99:
    music_russian_rap.append(data['response']['items'][k])
    k += 1
music_russian_rap_2 = []
for g in music_russian_rap:
    try:
        music_russian_rap_2.append(g['attachments'][1]['audio'])
    except KeyError:
        music_russian_rap_2.append('sos')
    except IndexError:
        music_russian_rap_2.append('sos')
vv = 0
while vv < 20:
    for x in music_russian_rap_2:
        if x == 'sos':
            music_russian_rap_2.remove(x)
    vv += 1
music_russian_rap_artist = []
music_russian_rap_title = []
v = 0
while v < len(music_russian_rap_2):
    music_russian_rap_artist.append(music_russian_rap_2[v]['artist'])
    v += 1
v = 0
while v < len(music_russian_rap_2):
    music_russian_rap_title.append(music_russian_rap_2[v]['title'])
    v += 1
music_russian_rap_dict = dict(zip(music_russian_rap_artist, music_russian_rap_title))
music_russian_rap_end = []
dd = 0
while dd < len(music_russian_rap_artist):
    ccc = []
    ccc.append(music_russian_rap_artist[dd])
    ccc.append(music_russian_rap_title[dd])
    music_russian_rap_end.append(ccc)
    dd += 1
russian_rap = []
for h in music_russian_rap_end:
    my_list = [' - '.join(h)]
    russian_rap.append(my_list)

data = requests.get(
    'https://api.vk.com/method/wall.get',
    params={
        "owner_id": -192590151,
        "count": 1000,
        "v": "5.92",
        "access_token": TOKEN

    }
).json()
frank_ocean = []
k = 0
while k < 10:
    frank_ocean.append(data['response']['items'][k])
    k += 1
frank_ocean_2 = []
for g in frank_ocean:
    frank_ocean_2.append(g['attachments'][0]['audio'])
vv = 0

frank_ocean_artist = []
frank_ocean_title = []
v = 0
while v < 10:
    frank_ocean_artist.append(frank_ocean_2[v]['artist'])
    v += 1
v = 0
while v < 10:
    frank_ocean_title.append(frank_ocean_2[v]['title'])
    v += 1
frank_ocean_end = []
dd = 0
while dd < len(frank_ocean_artist):
    ccc = []
    ccc.append(frank_ocean_artist[dd])
    ccc.append(frank_ocean_title[dd])
    frank_ocean_end.append(ccc)
    dd += 1
frank_ocean = []
for h in frank_ocean_end:
    my_list = [' - '.join(h)]
    frank_ocean.append(my_list)



import telebot  # импортируем модуль pyTelegramBotAPI
import conf     # импортируем наш секретный токен


telebot.apihelper.proxy = conf.PROXY
bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота


# этот обработчик запускает функцию send_welcome,
# когда пользователь отправляет команды /start или /help
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Это бот, который найдет для Вас новую музыку. Для дальнейшего использования введите команду /help")
@bot.message_handler(commands=['help'])
def send_genre(message):
    bot.send_message(message.chat.id,
                     "Напишите жанр: Russian pop, Rap, Italian Rap, French Rap, Indie, Russian Rap или Frank Ocean")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Russian pop':
        bot.send_message(message.from_user.id, random.choice(russian_pop));
    elif message.text == 'Rap':
        bot.send_message(message.from_user.id, random.choice(rap));
    elif message.text == 'Italian Rap':
        bot.send_message(message.from_user.id, random.choice(italian_rap));
    elif message.text == 'French Rap':
        bot.send_message(message.from_user.id, random.choice(french_rap));
    elif message.text == 'Indie':
        bot.send_message(message.from_user.id, random.choice(indie));
    elif message.text == 'Russian Rap':
        bot.send_message(message.from_user.id, random.choice(russian_rap));
    elif message.text == 'Frank Ocean':
        bot.send_message(message.from_user.id, random.choice(frank_ocean));
    else:
        bot.send_message(message.from_user.id, 'Проверьте правильность введенных данных')
if __name__ == '__main__':
        bot.polling(none_stop=True)

