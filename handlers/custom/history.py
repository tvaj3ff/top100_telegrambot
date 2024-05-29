from typing import List

from config_data.config import DATE
from loader import bot
from telebot.types import Message
from models.model_db import History, User


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user_id = message.from_user.id
    command = message.text
    user = User.get_or_none(User.user_id == user_id)
    date = DATE
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    history: List[History] = History.select(History.message)
    result = []
    result.extend(map(str, reversed(history)))
    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )

    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет истории")
        return
    text = '<br>Ваша история:</br>\n'
    bot.send_message(message.chat.id, text + '\n'.join(result), parse_mode='html')
