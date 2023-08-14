from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.loader import dp
from bot.utils.messages import get_me_message
from logger import logger


@dp.message_handler(Command('me'), chat_type=types.ChatType.SUPERGROUP)
async def start_user(message: types.Message):
    logger.info(f"{message.from_id} {message.text}")
    await message.answer(get_me_message(message), parse_mode=types.ParseMode.MARKDOWN_V2)
    try:
        await message.delete()
    except Exception as ex:
        logger.error(ex)

