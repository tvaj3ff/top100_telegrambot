from loader import bot
from telebot.types import Message
from models.model_db import User, History
from peewee import IntegrityError
from config_data.config import DATE


@bot.message_handler(commands=["start"], state=None)
def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    command = message.text
    date = DATE
    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, f"Приветствуем Вас в KinoMaster Bot {first_name} – вашем гиде по миру кино! 🌟"
                              f"Наш бот поможет вам открыть для себя топ-100 лучших фильмов всех "
                              f"времён и получить подробную информацию о каждом из них.")
    except IntegrityError:
        bot.reply_to(message, f"Рад Вас снова видеть в KinoMaster Bot, {first_name}!")

    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )
