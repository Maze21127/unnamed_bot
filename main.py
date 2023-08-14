from aiogram import Dispatcher, types
from aiogram.utils import executor

from bot.loader import dp
from logger import logger


async def set_default_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
    ])
    logger.info("Commands added")


async def on_startup(dispatcher: Dispatcher):
    await set_default_commands(dispatcher)
    logger.info("Bot start")


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("Bot shutdown")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
