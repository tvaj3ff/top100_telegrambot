from loader import bot
from telebot.types import Message
from api.api import movies_list
from models.model_card import get_card

top = movies_list[99]
card = get_card(top)


@bot.message_handler(commands=["low"])
def bot_high(message: Message):
    bot.send_message(message.chat.id, f"{card}", parse_mode='html')
