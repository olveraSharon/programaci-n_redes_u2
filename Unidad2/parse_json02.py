'''
Autor: Sharon Michelle Olvera Ibarra
Descripción: Invocando 
Fecha:23/10/2023
'''

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de Allende"
key = "vo4i3kCyleGvjQp8hBJpvxbvgNWvTC1q"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()


print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
#codificar para modificar el error distinto a cero
else :
    print(f"API Status: {json_status} = An ucsuccessful route call"  )

