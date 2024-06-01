from telebot.types import Message

from loader import bots


@bots.message_handler()
def bot_echo(message: Message):
    bots.reply_to(message, f'🤨 {message.from_user.first_name} Выберите действие!')
