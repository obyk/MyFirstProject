import requests
import config
import tokapi

proxy = config.proxy
appid = tokapi.appid

#погода
response = requests.post(config.Get_Weather,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = response.json()
condition = (data['weather'][0]['description'])
temp = (data['main']['temp'])

#прогноз на 10 дней
response = requests.post(config.Get_Forecast,proxies=proxy,params={'units': 'metric', 'lang': 'ru', 'APPID': appid})
data1 = response.json()
for i in data1['list']:
    (i['dt_txt'])[:16] + ' ' + '{0:+3.0f}'.format(i['main']['temp'])+ '°C' + ' ' + (i['weather'][0]['description'])

#прогноз на завтра
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
res=p+ ' '+p1+ ' '+p2+' ' +p3

