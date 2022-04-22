

import telebot
import requests
import bs4

TOKEN = "5388915598:AAHpezc8UkpCIPIPJzmbwwhU4MqzN4SZCL8"
bot = telebot.TeleBot(TOKEN)

def convert(num):
    i = float(num.replace(",", "."))
    return i


responce = requests.get('https://quote.rbc.ru/ticker/59090')
html = requests.get('https://quote.rbc.ru/ticker/72413')

# print(responce.status_code)
# print(html.status_code)

page = bs4.BeautifulSoup(responce.text, 'lxml')
page2 = bs4.BeautifulSoup(html.text, 'lxml')

item = page.find('span', class_="chart__info__sum")
usd = page2.find('span', class_="chart__info__sum")
bb = item.text[1:7]
EUR = convert(bb)
print("EUR = ", EUR)


aa = usd.text[1:7]
USD = convert(aa)
print("USD = ", USD)


@bot.message_handler(commands=["help"])
def heip(message: telebot.types.Message):
    text = 'Этот бот пересчитывает рубли в доллары или евро по текущему курсу ЦБ:\n <наберите ' \
           '/start>'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('eur')
        markup.row('usd')

        msg = bot.send_message(message.chat.id, 'Этот бот пересчитывает рубли в доллары или евро:\n Выберите валюту eur или usd', reply_markup=markup)
        bot.register_next_step_handler(msg, currency)


def currency(message):
    if message.text == 'eur':
        msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
        bot.register_next_step_handler(msg, eur)
    elif message.text == 'usd':
        msg = bot.send_message(message.chat.id, 'Введите сумму в рублях')
        bot.register_next_step_handler(msg, usd)
    else:
        msg = bot.send_message(message.chat.id, 'Введите корректные данные')
        bot.register_next_step_handler(msg, currency)


def eur(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / EUR)
    except ValueError:
        bot.send_message(message.chat.id, 'Введите данные в виде цифр')


def usd(message):
    try:
        bot.send_message(message.chat.id, float(message.text) / USD)
    except ValueError:
        bot.send_message(message.chat.id, 'Введите данные в виде цифр')


bot.polling()
