from loguru import logger

logger.add("logs/error/error.log", format="{time} {level} {message}", level="ERROR", rotation="50 MB")
logger.add("logs/info/info.log", format="{time} {level} {message}", level="INFO", rotation="50 MB")
logger.add("logs/debug/debug.log", format="{time} {level} {message}", level="DEBUG", rotation="50 MB")
