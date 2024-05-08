from loader import bot
from telebot.types import Message
from api.api import movies_list

top = movies_list


@bot.message_handler(commands=["top_100"])
def bot_high(message: Message):
    text = [f"{top[i]['rank']}. <b>{top[i]['title']}</b>" for i in range(len(top))]
    bot.send_message(message.chat.id, "\n".join(text), parse_mode='html')
