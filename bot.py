import sys
from os import environ

# noinspection PyPackageRequirements
import telebot

BOT_TOKEN = environ.get("BOT_TOKEN")

if BOT_TOKEN is None:
    sys.exit("Set BOT_TOKEN in environment variables")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """Добрый день! Это бот компании 'Бери Рули' Томск. Здесь вы сможете сделать предварительный заказ
    авто, оставить свои пожелания, оставить заявку для связи с менеджером.""")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
