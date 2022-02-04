import requests

APIKEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def search(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": APIKEY,
        "geocode": address,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def get_coords(address):
    toponym = search(address)
    coordinates = toponym["Point"]["pos"]
    longitude, latitude = map(float, coordinates.split(" "))
    return longitude, latitude


def get_ll_spn(address):
    toponym = search(address)
    lon, lat = get_coords(address)
    ll = ",".join(map(str, [lon, lat]))
    envelope = toponym["boundedBy"]["Envelope"]
    left, bottom = envelope["lowerCorner"].split(" ")
    right, top = envelope["upperCorner"].split(" ")
    lon = abs(float(left) - float(right))
    lat = abs(float(bottom) - float(top))
    spn = f"{lon},{lat}"
    return ll, spn
