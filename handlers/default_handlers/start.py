from telebot.types import Message

from loader import bots


@bots.message_handler(commands=['start'], content_types=['text'])
def handler_start(message: Message):
    bots.send_message(message.chat.id, f'🤓 Добрый день {message.from_user.first_name}! '
                                       f'я менеджер по поиску вакансий программистам, если я могу вам чем-то помочь '
                                       f'введите команду /custom'
                      )
