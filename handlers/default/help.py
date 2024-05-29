from telebot.types import Message
from loader import bot
from config_data.config import DEFAULT_COMMANDS, DATE
from models.model_db import History


@bot.message_handler(commands=["help"], state=None)
def bot_start(message: Message):
    user_id = message.from_user.id
    command = message.text
    date = DATE
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )
