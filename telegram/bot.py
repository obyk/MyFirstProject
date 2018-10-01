import telebot
import requests
import config

from telebot import apihelper
apihelper.proxy = {'https':'socks5://telegram:telegram@tkhpg.teletype.live:1080'}

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['ip'])
def Get_ip(message):
 ip_str = str (requests.get(config.Get_IP).content)
 ip = (ip_str.replace ('b','')).replace ("'",'')
 sent = bot.send_message(message.chat.id, ip)

proxy = {'http' : 'http://139.180.209.183:8080'}
appid = "3c6d91c05c75253f2514af4a8a8d3d2c"

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
    
        
if __name__ == '__main__':
     bot.polling(none_stop=True)



