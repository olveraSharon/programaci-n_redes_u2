'''
Autor: Sharon Michelle Olvera Ibarra
Descripción: Invocando 
Fecha:23/10/2023
'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        print("Hasta Luego")
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        print("Hasta Luego")
        break

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "vo4i3kCyleGvjQp8hBJpvxbvgNWvTC1q"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    else :
        print(f"API Status: {json_status} = An ucsuccessful route call"  )


