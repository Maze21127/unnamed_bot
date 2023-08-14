from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from bot.loader import dp
from bot.utils.messages import START_MESSAGE
from logger import logger


@dp.message_handler(CommandStart(), chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def start_user(message: types.Message):
    logger.info(f"{message.from_id} {message.text}")
    return await message.answer(START_MESSAGE)
