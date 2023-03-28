import telebot
import os
import datetime
import sys

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if BOT_TOKEN is None:
    sys.exit("Set BOT_TOKEN in environment variables")

bot = telebot.TeleBot(BOT_TOKEN)


 #  '''ОСНОВНАЯ ЧАСТЬ КОДА БОТА'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('Нет, в первый раз', 'Да, пользовался')
    bot.reply_to(message, f'Добрый день, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. Это бот компании "Бери Рули" Томск. Здесь вы сможете сделать предварительный заказ авто, оставить свои пожелания, оставить заявку для связи с менеджером. Пожалуйста, скажите, вы уже пользовались услугами нашей компании?',
                 reply_markup=user_markup, parse_mode="HTML")
    save_to_file(message)

def process_source_response(message):
    if message.text == 'Соцсети(Instagr.,VK)' or message.text == 'Друзья посоветовали' or message.text == 'Поисковики(Google, Yandex)' or message.text == 'Прочие источники':
        bot.reply_to(message, "Если вы не ознакомились с нашими принципами работы, пожалуйста, обязательно ознакомьтесь с договором аренды и условиями по ссылке: https://prokat-70.com/")
        bot.reply_to(message, "На какие даты вы бы хотели забронировать авто? (пример: 01.01.2023-05.01.2023)")
        save_to_file(message)
        # здесь можно добавить функцию для обработки дальнейшего диалога

    else:
        bot.reply_to(message, "Пожалуйста, выберите один из вариантов ответа.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Нет, в первый раз':
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Соцсети(Instagr.,VK)', 'Друзья посоветовали')
        user_markup.row('Поисковики(Google, Yandex)', 'Прочие источники')
        bot.reply_to(message, "Последний вопрос, перед тем, как мы перейдем к бронированию авто. Откуда вы о нас узнали?",
                     reply_markup=user_markup)
        bot.register_next_step_handler(message, process_source_response)
        save_to_file(message)
    elif message.text == 'Да, пользовался':
        user_markup = telebot.types.ReplyKeyboardMarkup()
        user_markup.row('Соцсети(Instagr.,VK)', 'Друзья посоветовали')
        user_markup.row('Поисковики(Google, Yandex)', 'Прочие источники')
        bot.reply_to(message, "Последний вопрос, перед тем, как мы перейдем к бронированию авто. Откуда вы о нас узнали?",
                     reply_markup=user_markup)
        bot.register_next_step_handler(message, process_source_response)
        save_to_file(message)

 #  Функция для сохранения ответов клиента, для статистики (работает)
def save_to_file(message):
    with open(r'C:/Users/Admin/Desktop/tests_2310066/BeriRuli_bot_logs/bot_answers.txt', 'a') as file:
        file.write(f'Name: {message.from_user.first_name} {message.from_user.last_name}\n')
        file.write(f'Date: {datetime.datetime.now()}\n')
        file.write(f'Answers: {message.text}\n')


 #  ''' ЧАСТЬ ДЛЯ РАБОТЫ С TRELLO'''
 #  Достаем данные из Trello, для сравнения дат бронирования
# import requests
#
# # Указать ключ API и токен доступа
# key = "f441cac8c351bbe4c43f34197e06d522"
# token = "ATTAce7ec4770983776f4852d55a604958bc34e038307abdc5e327710bd060854820AD686D15"
#
# # Указать ID доски и ID карточки
# board_id = "5wj9R3XQ"
# card_id = "your_card_id"
#
# # Формирование URL для запроса
# url = f"https://api.trello.com/1/boards/{board_id}/cards/{card_id}"
# querystring = {"key": key, "token": token}
#
# # Выполнение запроса и получение данных о карточке
# response = requests.request("GET", url, params=querystring)
# card_data = response.json()

#  СПОСОБ ОБХОДА ПРОБЛЕМЫ С ID КАРТОЧЕК:
#  url = f"https://api.trello.com/1/boards/{board_id}/cards?key={api_key}&token={api_token}"
# response = requests.get(url)
# cards = response.json()


 #  '''ОКОНЧАНИЕ ЧАСТИ РАБОТЫ С TRELLO'''



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()