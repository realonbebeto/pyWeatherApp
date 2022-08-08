from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

from ..utils import foreCast, geoCode

BASE_PATH = Path(__file__).resolve().parent

router = APIRouter(tags=['Weather'])
templates = Jinja2Templates(
    directory=str(BASE_PATH)+"/../templates/", autoescape=False, auto_reload=True)


@router.get("/index")
def getIndex():
    return {"title": "Weather App", "name": "Bebeto Nyamwamu"}


@router.get("/about")
def getAbout():
    return {"title": "Weather App", "name": "Bebeto Nyamwamu"}


@router.get("/help")
def getHelp():
    return {"title": "Help You", "name": "Bebeto Nyamwamu", "message": "Welcome, How may I help you"}


@router.get("/weather")
def getWeather(request: Request):
    return templates.TemplateResponse("weather.html", context={"request": request})


@router.post("/weather", response_class=HTMLResponse)
def getWeather(request: Request, query_loc: str = Form(...)):
    cast_response, place_name = foreCast(**geoCode(query_loc))
    weather_info = {"place_name": place_name,
                    "time": cast_response['current']['observation_time'],
                    "desc": cast_response['current']['weather_descriptions'][0],
                    "temp": cast_response['current']['temperature'],
                    "feels_like_temp": cast_response['current']['feelslike'],
                    "ccover": cast_response['current']['cloudcover'],
                    "rain": cast_response['current']['precip'],
                    "humidity": cast_response['current']['humidity'],
                    "swind": cast_response['current']['wind_speed'],
                    "icons": cast_response['current']['weather_icons'][0]}
    return templates.TemplateResponse("weather.html", context={"request": request, "weather_info": weather_info})
