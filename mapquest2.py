import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "QMQiVEdHs7rLfWLCVXBW8m5OcYOT1m1Y"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = Una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direccion desde " + (orig) + " hasta " + (dest))
        print("Duracion de viaje: " + (json_data["route"]["formattedTime"]))
        print("Millas: " + str(json_data["route"]["distance"]))
        print("Kilometros: " + str("{:.3f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.3f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")