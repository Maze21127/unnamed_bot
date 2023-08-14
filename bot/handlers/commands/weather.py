from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.loader import dp
from bot.utils.api.yandex.weather import get_weather
from bot.utils.messages import CITY_NOT_FOUND, get_weather_message
from bot.utils.weather import get_city_coords
from logger import logger


@dp.message_handler(Command('weather'), chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def weather(message: types.Message):
    logger.info(f"{message.from_id} {message.text}")
    args = message.get_args()
    coords = get_city_coords(args)
    city = args if args else "Владивосток"
    if coords:
        weather_data = await get_weather(coords)
        return await message.answer(get_weather_message(weather_data, city))
    return await message.answer(CITY_NOT_FOUND)

