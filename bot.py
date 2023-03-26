# import sys
# from os import environ
#
# # noinspection PyPackageRequirements
# import telebot
#
# BOT_TOKEN = environ.get("BOT_TOKEN")
#
# if BOT_TOKEN is None:
#     sys.exit("Set BOT_TOKEN in environment variables")
#
# bot = telebot.TeleBot(BOT_TOKEN)
#
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#
#
# bot.infinity_polling()


def message_for_client(*args, **kwargs):
    print('Вы всегда можете решить все вопросы, позвонив менеджеру')

message_for_client()