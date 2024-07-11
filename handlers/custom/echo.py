from loader import bot
from telebot.types import Message


@bot.message_handler(state=None)
def bot_echo(message: Message):
    if message.text == "Привет":
        bot.reply_to(message, "И Вам привет!")
    else:
        bot.reply_to(message, "Я Вас не понимаю")
