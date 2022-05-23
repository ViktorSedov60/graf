
import ast
import telebot
import time
from telebot import types
import requests
import json
import bs4

TOKEN = "5388915598:AAHpezc8UkpCIPIPJzmbwwhU4MqzN4SZCL8"
bot = telebot.TeleBot(TOKEN)


keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'юань': 'CNY',
    'рубль': 'RUB',
}



# responce = requests.get('https://www.cbr-xml-daily.ru/latest.js')
# aa = responce.json()
# aaa = (aa['rates'])
# data = aa['date']
# USD = aaa['USD']
# EUR = aaa['EUR']
#
# rub_eur = round(1 / EUR, 2)
# rub_usd = round(1 / USD, 2)
#
# print('На дату: ', data)
# print('за рубль дадут :', USD, '  долларов')
# print('за рубль дадут:', EUR, ' евро')
# print('за доллар отдать :', rub_usd, " рублей")
# print('за евро отдать :', rub_eur, ' рублей')


# @bot.message_handler(commands=["help"])
# def help(message: telebot.types.Message):
#     text = f'Этот бот пересчитывает рубли в доллары или евро по текущему курсу ЦБ: \n ' \
#            f'сегодня за евро {rub_eur} рублей  \n за доллар  {rub_usd} рублей  \n наберите ' \
#            ' /start \n увидеть доступный список валют:  /values'
#     bot.reply_to(message, text)

def makeKeyboard():
    markup = types.InlineKeyboardMarkup()

    for key, value in keys.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "']")),


    return markup


print(keys.values())



# @bot.message_handler(commands=["values"])
# def values(message: telebot.types.Message):
#     text = 'Доступные валюты: '
#     for key in keys.keys():
#         text = '\n'.join((text, key, ))
#     bot.reply_to(message, text)




# def valut(message):
#     quote = telebot.types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#
#     for key, value in keys.items():
#         quote.add(types.InlineKeyboardButton(text=value, callback_data="['value', '" + value + "']")
#     return quote

# def start2(message):
#
#     if quote != '':
#
#         markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#         markup.row('список валют на которую меняем')
#         # markup.row('usd')
#
#         msg1 = bot.send_message(message.chat.id, 'Этот бот пересчитывает рубли в доллары или '
#                                                'евро:\n Выберите валюту eur или usd', reply_markup=markup)
#         bot.register_next_step_handler(msg1, valut1)
#
# def valut1(message):
#     base = types.InlineKeyboardMarkup()
#
#     for key, value in keys.items():
#         base.add(types.InlineKeyboardButton(text=value, callback_data="['value', '" + value + "']")
#     return base


# def currency(message):
#     if message.text == 'eur':
#         text = f'Сегодня   {data}  за рубль  дадут   {EUR}   евро, или за Евро  {rub_eur}  рублей'
#         bot.reply_to(message, text)
#         # bot.reply_to(message, EUR)
#         msg = bot.send_message(message.chat.id, 'Введите сумму в рублях и узнайте сколько это евро')
#         bot.register_next_step_handler(msg, eur)
#
#     elif message.text == 'usd':
#         text = f'Сегодня   {data}   за рубль дадут   {USD}   долларов, или за Доллар {rub_usd}  рублей'
#         bot.reply_to(message, text)
#         # bot.reply_to(message, USD)
#         msg = bot.send_message(message.chat.id, 'Введите сумму в рублях и узнайте сколько это '
#                                                 'долларов')
#         bot.register_next_step_handler(msg, usd)
#     else:
#         msg = bot.send_message(message.chat.id, 'Введите корректные данные')
#         bot.register_next_step_handler(msg, currency)
#
#
# def eur(message):
#     try:
#         bot.send_message(message.chat.id, round(float(message.text) * EUR, 2))
#
#     except ValueError:
#         bot.send_message(message.chat.id, 'Введите данные в виде цифр')
#
#
# def usd(message):
#     try:
#         bot.send_message(message.chat.id, round(float(message.text) * USD, 2))
#
#     except ValueError:
#         bot.send_message(message.chat.id, 'Введите данные в виде цифр')
#
#


# bot.polling()


