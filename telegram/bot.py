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

proxy = {'http': 'http://64.13.147.154:60837'}
appid = config.appid

        

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



