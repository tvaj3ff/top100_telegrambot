from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    get_movie_info = State()
