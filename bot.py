ahahah - aha-aha-ahahaaaaahh

import telebot
import requests
import config

from telebot import types
from telebot import apihelper
apihelper.proxy = {'https':'socks5://telegram:telegram@tkhpg.teletype.live:1080'}

bot = telebot.TeleBot(config.token)
proxy = config.proxy
appid = config.appid

@bot.message_handler(commands=['ip'])
def Get_ip(message):
 ip_str = str (requests.get(config.Get_IP).content)
 ip = (ip_str.replace ('b','')).replace ("'",'')
 sent = bot.send_message(message.chat.id, ip)

@bot.message_handler(commands=['погода'])
def Get_weather_mess(message):
    response = requests.post(config.Get_Weather,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = response.json()
    condition = (data['weather'][0]['description'])
    temp = (data['main']['temp'])
    sent = bot.send_message(message.chat.id, str(condition) + ' ' + str(temp) + '°C')

@bot.message_handler(commands=['прогноз'])
def Get_forecast_mess(message):
    response = requests.post(config.Get_Forecast,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = response.json()
    for i in data['list']:
        bot.send_message(message.chat.id, (i['dt_txt'])[:16] + ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ '°C' + ' ' + (i['weather'][0]['description']))

# переменные для вывода данных текущей погоды
response = requests.post(config.Get_Weather,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = response.json()
condition = (data['weather'][0]['description'])
temp = (data['main']['temp'])
resul = str(condition) + ' ' + str(temp) + '°C'

#переменные для вывода данных прогноза погоды
response = requests.post(config.Get_Forecast,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = response.json()
cond = (data['list'][7]['weather'][0]['description'])
day = (data['list'][7]['dt_txt'][:16])
tem = (data['list'][7]['main']['temp'])
p = day+' '+ '{0:+3.0f}'.format(tem)+ '°C'+ ' ' + cond
cond1 = (data['list'][8]['weather'][0]['description'])
day1 = (data['list'][8]['dt_txt'][:16])
tem1 = (data['list'][8]['main']['temp'])
p1 = day1+' '+ '{0:+3.0f}'.format(tem1)+ '°C'+ ' ' + cond1
cond2 = (data['list'][9]['weather'][0]['description'])
day2 = (data['list'][9]['dt_txt'][:16])
tem2 = (data['list'][9]['main']['temp'])
p2 = day2+' '+ '{0:+3.0f}'.format(tem2)+ '°C'+ ' ' + cond2
cond3 = (data['list'][10]['weather'][0]['description'])
day3 = (data['list'][10]['dt_txt'][:16])
tem3 = (data['list'][10]['main']['temp'])
p3= day3+' '+ '{0:+3.0f}'.format(tem3)+ '°C'+ ' ' + cond3

@bot.message_handler(commands=['привет'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add('Погода') #Имена кнопок
    msg = bot.reply_to(message, 'Привет!', reply_markup=markup)
    
# создаем кнопки
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="погода", callback_data="n1")
    callback_button1 = types.InlineKeyboardButton(text="прогноз", callback_data="n2")
    keyboard.add(callback_button,callback_button1 )
    bot.send_message(message.chat.id, "Хотите узнать погоду?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "n1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=resul)
        if call.data == "n2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=p1+' '+p2+' '+p3)
        
if __name__ == '__main__':
     bot.polling(none_stop=True)



