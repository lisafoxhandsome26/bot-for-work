from telebot.types import Message

from API_requests.site_req import make_request
from loader import bots
from KeyBoards.reply import replyKeyboards
from KeyBoards.inline import inlineKeyboards
from databasa import req_to_base_data

language = None
country = None

data_country = ('🇷🇺 Russia', '🇺🇸 USA', '🇨🇳 China', '🇩🇪 Germany', '🇫🇷 France', '🇬🇧 Great Britany')
data_languages = ('Python', 'Java', 'C++', 'C#', 'JavaScript', 'PHP')


@bots.message_handler(commands=['custom'], content_types=['text'])
def handler_custom(message: Message):
    murkup = replyKeyboards.buttons(data_languages)
    bots.send_message(message.chat.id, '🤓 Какой язык програмирования предпочитаете?', reply_markup=murkup)
    bots.register_next_step_handler(message, call_backs)


def call_backs(message: Message):
    murkup = replyKeyboards.buttons(data_country)
    bots.send_message(message.chat.id, '🤓 Где будем искать?', reply_markup=murkup)

    global language
    language = message.text.strip()
    bots.register_next_step_handler(message, check_local)


def check_local(message: Message):
    global country
    check_word = message.text.strip()
    country = check_word
    if check_word in data_country:
        country = check_word[3:]

    murk = inlineKeyboards.buttons_inl()
    bots.send_message(message.chat.id, '🤓 Выберите ожидаемый уровень зароботной платы', reply_markup=murk)


@bots.callback_query_handler(func=lambda callback: True)
def call_back(callback):
    murkup = replyKeyboards.base_buttons()
    message = f'🤓 Ваш язык {language}, локация {country}.\n' \
              f'ожидаемый уровень зарабатных плат {callback.data}'

    urlist = {"query": f"{language} developer in {country}", "page": "1", "num_pages": "1"}
    bots.send_message(callback.message.chat.id, f'{message}\nВыполняем запрос...', reply_markup=murkup)
    set_message = make_request(urlist, callback.data)

    if not set_message.startswith('Ошибка'):
        user = callback.message.chat.id
        req_to_base_data.datas = {'user_id': user, 'message': message, 'self_req': urlist}
        req_to_base_data.write_datas()

    bots.send_message(callback.message.chat.id, set_message, reply_markup=murkup)
