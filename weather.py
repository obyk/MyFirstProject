import requests
import config
import tokapi


#погода
response = requests.post(tokapi.Get_Weather,params={'units': 'metric', 'lang': 'ru'})
data = response.json()
condition = str(data['current']['condition']['text'])
temp = str(data['current']['temp_c'])
current = condition + ' ' + temp + '°C'

#прогноз на 7 дней
response = requests.post(tokapi.Get_Forecast,params={'units': 'metric', 'lang': 'ru'})
data1 = response.json()
for i in data1['forecast']['forecastday']:
    forecast = str(i['date']) + ' ' + (str(i['day']['avgtemp_c']))+ '°C' + ' ' + (str(i['day']['condition']['text']))

#прогноз на завтра
response = requests.post(tokapi.Get_Forecast,params={'units': 'metric', 'lang': 'ru'})
data = response.json()
cond = str(data['forecast']['forecastday'][1]['day']['condition']['text'])
day = str(data['forecast']['forecastday'][1]['date'])
tem = str(data['forecast']['forecastday'][1]['day']['avgtemp_c'])
resul = day + ' ' + tem + '°C' + ' ' + cond
