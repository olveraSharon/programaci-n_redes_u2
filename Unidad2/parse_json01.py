'''
Autor: Sharon Michelle Olvera Ibarra
Descripción: Invocando 
Fecha:23/10/2023
'''

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de Allende"
key = "vo4i3kCyleGvjQp8hBJpvxbvgNWvTC1q"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])

#Extrae la distancia y el tiempo
distance=json_data ['route']['distance']
time=json_data ['route']['time']
print({distance},{time})
#Extrae del primer elemento formatetime
formattedTime=json_data['route']['legs'][0]['formattedTime']
print({formattedTime})