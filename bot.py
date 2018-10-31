import telebot
import requests
import config
import tokapi
import weather

from telebot import types
from telebot import apihelper
apihelper.proxy = {'https':'socks5://telegram:telegram@tkhpg.teletype.live:1080'}

bot = telebot.TeleBot(tokapi.token)
proxy = config.proxy
appid = tokapi.appid

@bot.message_handler(commands=['ip'])
def Get_ip(message):
 ip_str = str (requests.get(config.Get_IP).content)
 ip = (ip_str.replace ('b','')).replace ("'",'')
 sent = bot.send_message(message.chat.id, ip)

@bot.message_handler(commands=['прогноз'])
def Get_forecast_mess(message):
    data = weather.data1
    for i in data['list']:
        bot.send_message(message.chat.id, (i['dt_txt'])[:16] + ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ '°C' + ' ' + (i['weather'][0]['description']))

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
    callback_button1 = types.InlineKeyboardButton(text="погода завтра", callback_data="n2")
    callback_button2 = types.InlineKeyboardButton(text="прогноз на 10 дней", callback_data="n3")
    keyboard.add(callback_button,callback_button1)
    keyboard.add(callback_button2)
    bot.send_message(message.chat.id, "Хотите узнать погоду?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "n1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(weather.condition) + ' ' + str(weather.temp) + '°C')
        if call.data == "n2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=weather.res)
        elif call.data == "n3":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введите команду '/прогноз'")
        
if __name__ == '__main__':
     bot.polling(none_stop=True)



