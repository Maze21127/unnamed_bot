import aiohttp
import pydantic

from settings import YANDEX_WEATHER_API_KEY

WEATHER_URL = "https://api.weather.yandex.ru/v2/informers"
WEATHER_HEADERS = {
    "X-Yandex-API-Key": YANDEX_WEATHER_API_KEY
}


CONDITIONS = {
    "clear": "Ясно",
    "partly-cloudy": "малооблачно",
    "cloudy": "облачно с прояснениями",
    "overcast": "пасмурно",
    "light-rain": "небольшой дождь",
    "rain": "дождь",
    "heavy-rain": "сильный дождь",
    "showers": "ливень",
    "wet-snow": "дождь со снегом",
    "light-snow": "небольшой снег",
    "show": "снег",
    "snow-showers": "снегопад",
    "hail": "град",
    "thunderstorm": "гроза",
    "thunderstorm-with-rain": "дождь с грозой",
    "thunderstorm-with-hail": "гроза с градом"
}


class Weather(pydantic.BaseModel):
    temp: float
    condition: str
    wind_speed: float
    humidity: float


async def get_weather(params: dict):
    async with aiohttp.ClientSession(headers=WEATHER_HEADERS) as session:
        async with session.get(WEATHER_URL, params=params) as response:
            data = await response.json()
            weather_data = Weather(
                temp=data['fact']['temp'],
                condition=CONDITIONS.get(data['fact']['condition'], None),
                wind_speed=data['fact']['wind_speed'],
                humidity=data['fact']['humidity']
            )
            return weather_data

