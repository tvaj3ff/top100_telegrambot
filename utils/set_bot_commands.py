from config_data import config
from telebot.types import BotCommand


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*cmd) for cmd in config.DEFAULT_COMMANDS]
    )
