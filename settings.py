from dotenv import load_dotenv
import envparse

load_dotenv(".env")

BOT_TOKEN = envparse.env("BOT_TOKEN")
