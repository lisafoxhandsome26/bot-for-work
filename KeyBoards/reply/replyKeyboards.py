from telebot import telebot, types

from config_data.config import DEFAULT_COMMANDS as dat


def base_buttons():
    murkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton(dat[0])
    bt2 = types.KeyboardButton(dat[1])
    bt3 = types.KeyboardButton(dat[2])
    bt4 = types.KeyboardButton(dat[3])
    murkup.row(bt1, bt2)
    murkup.row(bt3, bt4)
    return murkup


def buttons(data):
    murkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton(data[0])
    bt2 = types.KeyboardButton(data[1])
    bt3 = types.KeyboardButton(data[2])
    bt4 = types.KeyboardButton(data[3])
    bt5 = types.KeyboardButton(data[4])
    bt6 = types.KeyboardButton(data[5])
    murkup.row(bt1, bt2, bt3)
    murkup.row(bt4, bt5, bt6)
    return murkup
