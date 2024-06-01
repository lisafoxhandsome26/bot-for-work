from telebot import types


def buttons_inl():
    murk = types.InlineKeyboardMarkup()
    low = types.InlineKeyboardButton('/low', callback_data='низкие')
    high = types.InlineKeyboardButton('/high', callback_data='высокие')
    murk.add(low, high)
    return murk
