from loader import bot
from telebot.types import Message


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!", parse_mode='html')