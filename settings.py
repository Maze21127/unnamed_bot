from dotenv import load_dotenv
import envparse

load_dotenv(".env")

BOT_TOKEN = envparse.env("BOT_TOKEN")
YANDEX_WEATHER_API_KEY = envparse.env("YANDEX_WEATHER_API_KEY")
