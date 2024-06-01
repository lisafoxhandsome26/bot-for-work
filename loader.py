from telebot import TeleBot
from config_data import config


bots = TeleBot(token=config.BOT_TOKEN)
