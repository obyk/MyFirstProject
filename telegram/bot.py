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
for i in data['list'][7:9]:
    cond = (i['weather'][0]['description'])
    day = (i['dt_txt'][:16])
    tem = (i['main']['temp'])
    prognoz = (i['dt_txt'])[:16] + ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ '°C' + ' ' + (i['weather'][0]['description'])

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
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=prognoz)
            
    

    
        
if __name__ == '__main__':
     bot.polling(none_stop=True)



