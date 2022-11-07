import telebot
from telebot import types
import requests
from config import TOKEN 
from config import APIKEYS
# from pyown import OWN
# from pyown.utils.config import get_default_config

# owm = pyowm.OWM(APIKEYS)
# place = input("В каком городе/стране?: ") # Пользователь вводит город в импут

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('London,GB')
# w = observation.get_weather()
# print(w)

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Привет, {message.from_user.first_name}'
#     bot.send_message(message.chat.id, mess, parse_mode = 'html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет':
        mess = f'И тебе привет, {message.from_user.first_name}, жмакни кнопку'
        bot.send_message(message.chat.id, mess, parse_mode = 'html')  
    elif message.text == 'Погода':
      bot.send_message(message.chat.id, "жмакни кнопку", parse_mode = 'html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode = 'html')  

@bot.message_handler(commands=['help'])
def weath(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Узнать погоду')
    item2 = types.KeyboardButton('Курсы валют')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет, {0}!'.format(message.from_user.first_name), reply_markup=markup)

@bot.message_handler(content_types=['button'])
def bot_message(message):
    if message.chat.type == 'private':       
        if message.text == 'Узнать погоду':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('На Сегодня')
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)

            bot.send_message(message.chat.id, 'держи', reply_markup=markup)


        elif message.text == 'Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Курс Доллара')
            item2 = types.KeyboardButton('Курс Евро')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Курсы валют', reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Узнать погоду')
            item2 = types.KeyboardButton('Курсы валют')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode = 'html')  

bot.polling(none_stop = True)
