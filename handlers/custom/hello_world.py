from telebot.types import Message

from config_data.config import DATE
from loader import bot
from models.model_db import History

anecdote = ('традиция использования фразы «Hello, world!» в качестве тестового сообщения была введена '
            'в книге «Язык программирования Си» Брайана Кернигана и Денниса Ритчи, опубликованной в 1978 году.')


@bot.message_handler(commands=["hello_world"], state="*")
def bot_helloworld(message: Message):
    user_id = message.from_user.id
    command = message.text
    date = DATE
    bot.reply_to(message, f"{message.from_user.first_name}, знаете ли вы, что: \n{anecdote}")
    History.create(
        user_id=user_id,
        created_at=date,
        message=command
    )