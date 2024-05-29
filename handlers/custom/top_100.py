from config_data.config import DATE
from loader import bot
from telebot.types import Message

from models.model_db import History
from states.user_state import UserState
from api.api import movies_list
from models.model_card import get_card


top = movies_list


@bot.message_handler(state="*", commands=["top_100"])
def bot_high(message: Message) -> None:
    user_id = message.from_user.id
    command = message.text
    date = DATE
    bot.set_state(message.from_user.id, UserState.get_movie_info)
    text = [f"{top[i]['rank']}. <b>{top[i]['title']}</b>" for i in range(len(top))]
    bot.send_message(message.chat.id, "\n".join(text), parse_mode='html')
    bot.send_message(message.chat.id,
                     "Для получения дополнительной информации об одном из фильмов спиcка,"
                     " введите его номер.",
                     parse_mode='html')
    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )



@bot.message_handler(state=UserState.get_movie_info)
def get_movie_num(message: Message) -> None:
    msg = message.text
    if (msg.isdigit()) and (1 <= int(msg) <= 100):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['movie'] = int(message.text)
            card = get_card(top[data['movie'] - 1])
            bot.send_message(message.chat.id, f"{card}", parse_mode='html')

    else:
        bot.send_message(message.chat.id,
                         "Номер должен быть цифровым и находиться в диапазоне от 1 до 100.",
                         parse_mode='html')

