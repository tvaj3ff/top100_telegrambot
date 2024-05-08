import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "запуск"),
    ("high", "Вывод фильм #1"),
    ("low", "Вывод фильм #100"),
    ("top_100", "Список топ 100"),
    ("hello_world", "Анекдот"),
    ("help", "помощь с командами")
)
