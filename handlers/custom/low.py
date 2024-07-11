from config_data.config import DATE
from loader import bot
from telebot.types import Message
from api.api import movies_list
from models.model_card import get_card
from models.model_db import History

top = movies_list[99]
card = get_card(top)


@bot.message_handler(commands=["low"])
def bot_high(message: Message):
    user_id = message.from_user.id
    command = message.text
    date = DATE
    bot.send_message(message.chat.id, f"{card}", parse_mode='html')
    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )