import requests
import datetime
import telebot
import tokapi
import weather
import config


from telebot import types
from telebot import apihelper
apihelper.proxy = {'https':'socks5://telegram:telegram@tkhpg.teletype.live:1080'}

bot = telebot.TeleBot(tokapi.token)
now = datetime.datetime.now()
today = now.day
time = now.hour
cond = weather.cond

for user in config.users:
    if cond == 'Местами дождь' or cond== 'Дождь' and today == now.day and time == 20:
        bot.send_message(user, 'Завтра возможен дождь. Не забудь зонт! Приятного вечера')
        today+=1 
    if 'снег' in cond and today == now.day and time >= 20:
        bot.send_message(user, 'Завтра ожидается снег. Будь осторожен за рулем! Приятного вечера')
        today+=1   
    elif today == now.day and time >= 20:
        bot.send_message(user, 'Осадков не  ожидается. Приятного вечера')
        today+=1 


