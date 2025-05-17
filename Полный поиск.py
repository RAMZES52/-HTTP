import geo_functions
import sys
from io import BytesiO
import requests
from PIL import Image

if len(sys.argv) <= 1:
    print("No data")
    exit(0)
toponym_to_find = " ".join(sys.argv[1:])
toponym = geo_functions.geocode(toponym_to_find)
toponym_coodrinates = geo_functions.get_coordinates(toponym_to_find)
ll, spn = geo_functions.get_ll_span(toponym_to_find)
delta = "0.005"
map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    "pt": ll
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesiO(response.content)).show()
