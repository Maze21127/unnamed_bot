from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.loader import dp
from bot.utils.messages import get_me_message
from logger import logger


@dp.message_handler(Command('me'), chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP])
async def me_handler(message: types.Message):
    logger.info(f"{message.from_id} {message.text}")
    if not message.get_args():
        return
    await message.answer(get_me_message(message), parse_mode=types.ParseMode.MARKDOWN_V2)
    try:
        await message.delete()
    except Exception as ex:
        logger.error(ex)

