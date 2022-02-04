import sys
import requests
import Geocoder_search


def set_map_params(ll, spn):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        "pt": "{0},pm2dgl".format(ll)
    }
    return map_params


def make_map(map_params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def search(address):
    ll, spn = Geocoder_search.get_ll_spn(address)
    map_params = set_map_params(ll, spn)
    make_map(map_params)
    return ll, spn
