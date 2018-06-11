# -*- coding: utf-8 -*-

import random
import json
#import urllib
#from lxml import html
#import requests
from botocore.vendored import requests

def point(event, context):
    print(event)
    myChatID = '-194424605'
    send_message(myChatID, json.dumps(event))
    # достанем ChatID (для message и edited_message)
    message_key = 'message'
    message = event.get(message_key, None)
    if message == None:
        message_key = 'edited_message'
        message = event.get(message_key, None)
    chat_id = message['chat']['id']

    if event[message_key]["text"][0] == "/":
        words = event[message_key]["text"].split()
        command = words[0][1:]
        first_name = event[message_key]["chat"]["first_name"]
        command_answer(command, chat_id, first_name, words)

    else:
        if event[message_key]["from"]["username"] == 'iv_rom':
            send_message(event[message_key]["chat"]["id"], "Давай по новой, Ваня, переписываем!")
        else:
            send_message(event[message_key]["chat"]["id"], "Введите команду. Формат команды следующий: /<имя команды> [<параметр1>]")



def command_answer(command, chat_id, first_name, words):
    if command == 'echo' or command == 'echo@klokybot':
        send_message(chat_id, "бот робиц")

    elif command == 'start' or command == 'start@klokybot':
        HELLO = [
            "Привет",
            "Приветствую",
            "Доброго времени суток"
        ]
        hello_text = "{hi}, {username}!".format(
            hi = random.choice(HELLO),
            username = first_name
        )
        send_message(chat_id, hello_text)

    elif command == 'help' or command == 'help@klokybot':
        help_text = "Боту надо ввести команду, дядя!\n /echo - узнать работоспособность,\n /joke - получить АКБ,\n /start - хоть где-то с тобой поздоровается."
        send_message(chat_id, help_text)

    elif command == "joke" or command == 'joke@klokybot':
        JOKES_DICT = [
            "На детский утренник сын Елены Малышевой пришел в костюме тромба и оторвался по полной.",
            "Можно шутить про что угодно, кроме мексиканцев, ведь это переходит все границы.",
            "Дочери Владимира Путина не пойдут на выборы, потому что родителей не выбирают.",
            "Что говорит гей-шмель своему партнёру?\nЖаль.",
            "Житель российской глубинки вышел на улицу и случайно посмотрел «Левиафан».",
            "Идёт по улице владелец Xiaomi в одном ботинке. Навстречу ему мужик:\n— Что, ботинок потерял?\n— Нет, нашёл.",
            "Мальчик, воспитанный воблой, при виде пива начинал биться головой об стол.",
            "— Это квартира Ивана Ивановича Тупого?\n— Аааам… Эээээ… не понял вопроса.",
            "— Мужчина, у вас в ухе банан!\n— Говорите громче, у меня в ухе банан!"
        ]
        send_message(chat_id, random.choice(JOKES_DICT))

    elif command == "photo":
        link = words[1]
        linkList = link.split('.')
        extension = linkList[len(linkList) - 1]
        ext_list = ['ras','xwd','bmp','jpe','jpg','jpeg','xpm','ief','pbm','tif','gif','ppm','xbm','tiff','rgb','pgm','png','pnm']
        if extension in ext_list:
            send_photo(chat_id, link)
        else:
        #    page = html.fromstring(urllib.urlopen(photolink).read())
        #    pic_url = ""
        #    for link in page.xpath("//a"):
        #        link_str = str(link.get("href"))
        #        if link_str.find('userapi') > 0 and link_str.find('jpg') > 0:
        #            pic_url = link.get("href")
        #    if pic_url != "":
        #        send_photo(event["message"]["chat"]["id"], photolink)
        #    else:
            send_message(chat_id, "Это точно ссылка на фото?")
    else:
        send_message(chat_id, "Я не знаю эту команду")




def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="yourToken",
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data = data)
    print(r.json())

def send_photo(chat_id, photo):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="yourToken",
        method="sendPhoto"
    )
    data = {
        "chat_id": chat_id,
        "photo": photo
    }
    r = requests.post(url, data = data)
    print(r.json())
