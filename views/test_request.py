# import requests

# url = "https://community-open-weather-map.p.rapidapi.com/weather"

# querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"Belo Horizonte"}

# headers = {
#     'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
#     'x-rapidapi-key': "3c901258b9msh6ec595fafe09858p1db3cbjsn7cc6553765cf"
#     # 'x-rapidapi-key': "ac7c75b9937a495021393024d0a90c44"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)


import requests
import pprint

api_address='http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Belo Horizonte,br'
url = api_address + city + r'&units=metric&lang=pt' 
json_data = requests.get(url).json()
# format_add = json_data['base']
# print(format_add)



pprint.pprint(json_data)




auaheuirhaseiutrha

dados = json_data['list'][0]
dataold = dados['dt_txt'].split()[0]
dias = []
infodia = {}
cnt = 1
temp = dados['main']['temp']
tempmin = dados['main']['temp_min']
tempmax = dados['main']['temp_max']
clima = [dados['weather'][0]['description']]

for i in json_data['list'][1:]:
	datanew = i['dt_txt'].split()[0]
	if datanew !=  dataold:
		infodia['dia'] = dataold
		infodia['num'] = cnt
		infodia['temp'] = round(temp/max(cnt, 1), 2)
		infodia['temp_min'] = round(tempmin/max(cnt, 1), 2)
		infodia['temp_max'] = round(tempmax/max(cnt, 1), 2)
		infodia['clima'] = max(clima, key = clima.count)
		dias.append(infodia)
		infodia = {}
		temp = 0
		tempmin = 0
		tempmax = 0
		cnt = 0
		clima = []
		dataold = datanew

	cnt+=1
	temp += i['main']['temp']
	tempmin += i['main']['temp_min']
	tempmax += i['main']['temp_max']
	clima.append(i['weather'][0]['description'])


infodia['dia'] = dataold
infodia['num'] = cnt
infodia['temp'] = round(temp/max(cnt, 1), 2)
infodia['temp_min'] = round(tempmin/max(cnt, 1), 2)
infodia['temp_max'] = round(tempmax/max(cnt, 1), 2)
infodia['clima'] = max(clima, key = clima.count)
dias.append(infodia)
infodia = {}
temp = 0
tempmin = 0
tempmax = 0
cnt = 0



# pprint.pprint(json_data)
pprint.pprint(dias)

# for key in json_data:
# 	print(key)
# 	print(json_data[key], '\n')