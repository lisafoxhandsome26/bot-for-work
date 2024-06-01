from telebot.types import Message

from loader import bots


@bots.message_handler(commands=['help'], content_types=['text'])
def handler_help(message: Message):
    bots.send_message(message.chat.id, '📌 /start – команда выводит приветствие пользователю.')
    bots.send_message(message.chat.id, '📌 /custom – команда формирует запрос:\n'
                                       '- Бот запрашивает пользователя выбрать или ввести язык программирования\n'
                                       '- Бот запрашивает пользователя выбрать или ввести название локации\n')
    bots.send_message(message.chat.id, '📌 /history – команда выводит историю запросов пользователя\n'
                                       '*По умолчанию максимальное количество запросов - 5.')
    bots.send_message(message.chat.id, '📌 /low – команда выводит ответы с минимальными зароботными платами.\n'
                                       '*По умолчанию Бот выводит 5 ответов, если Бот получит меньше 5 ответов, '
                                       'Бот выведит все что получит.')
    bots.send_message(message.chat.id, '📌 /high – команда выводит ответы с максимальными зароботными платами.\n'
                                       '*По умолчанию Бот выводит 5 ответов, если Бот получит меньше 5 ответов, '
                                       'Бот выведит все что получит.')
    bots.send_message(message.chat.id, '📌 /help - помощь по командам Бота.')
