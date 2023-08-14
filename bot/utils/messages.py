from aiogram import types

from bot.utils.api.yandex.weather import Weather

START_MESSAGE = "Бот активирован"
CITY_NOT_FOUND = "Город не найден"
WEATHER_MESSAGE = """
Погода в городе {city}
Температура {temp} °C, {condition}
Влажность: {humidity}%
Скорость ветра: {wind_speed} м/с
"""


def get_me_message(message: types.Message) -> str:
    arguments = message.get_args()
    user = message.from_user
    if user.first_name:
        return f"*{user.first_name}* {arguments}"
    if user.username:
        return f"**{user.username}** {arguments}"
    # А если у пользователя нет ни имени, ни ника? Ситуация редкая, но надо обработать.
    return "message"


def get_weather_message(weather_data: Weather, city: str):
    return WEATHER_MESSAGE.format(
        city=city.capitalize(),
        temp=weather_data.temp,
        condition=weather_data.condition,
        humidity=weather_data.humidity,
        wind_speed=weather_data.wind_speed
    )
