import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DB_PATH = "database.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

DEFAULT_COMMANDS = (
    ("start", "запуск"),
    ("history", "история запросов"),
    ("help", "помощь с командами"),
    ("high", "Фильм #1"),
    ("low", "Фильм #100"),
    ("top_100", "Список топ-100"),
    ("hello_world", "Анекдот"),
)

DATE_FORMAT = "%d.%m.%Y"
DATE = datetime.today().date().strftime(DATE_FORMAT)
