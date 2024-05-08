from telebot.types import Message
from loader import bot

anecdote = ('традиция использования фразы «Hello, world!» в качестве тестового сообщения была введена '
            'в книге «Язык программирования Си» Брайана Кернигана и Денниса Ритчи, опубликованной в 1978 году.')


@bot.message_handler(commands=["hello_world"])
def bot_helloworld(message: Message):
    bot.reply_to(message, f"{message.from_user.first_name}, знаете ли вы, что: \n{anecdote}")
