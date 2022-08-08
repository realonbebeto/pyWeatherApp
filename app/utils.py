import requests
from urllib.parse import quote

from .config import settings


def geoCode(location):
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + \
        quote(location.encode('utf8')) + \
        f".json?access_token={settings.geo_access_token}&limit=1"

    try:
        r = requests.get(url).json()  # ['features']
        return {"lat": r['features'][0]['center'][1], "lon": r['features'][0]['center'][0], "location": r['features'][0]['place_name']}

    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        raise SystemExit(e)


def foreCast(lat, lon, location):
    url = f"http://api.weatherstack.com/current?access_key={settings.meteo_access_token}&query=" + quote(
        str(lat)) + "," + quote(str(lon))

    try:
        r = requests.get(url)
        return r.json(), location

    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        raise SystemExit(e)
