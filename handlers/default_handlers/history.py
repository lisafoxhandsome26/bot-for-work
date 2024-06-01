from telebot.types import Message

from loader import bots
from databasa.req_to_base_data import select_datas


@bots.message_handler(commands=['history'], content_types=['text'])
def handler_custom(message: Message):
    try:
        res = select_datas(message.chat.id)

        bots.send_message(message.chat.id, 'Ваша история запросов:')
    finally:
        if res:
            bots.send_message(message.chat.id, res)
        else:
            bots.send_message(message.chat.id, 'Ошибка: история запросов пуста')
