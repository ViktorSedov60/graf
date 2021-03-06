import ast
import time
from config import token, keys
import telebot
from telebot import types
import requests



bot = telebot.TeleBot(token)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


# сгенерируем столбцы с кнопками согласно списка валют
def makeKeyboard():
    markup = types.InlineKeyboardMarkup()

    for key, value in keys.items():
        markup.add(types.InlineKeyboardButton(text=key,
                                              callback_data="['value', '" + value + "', '" + key + "']"),
                   types.InlineKeyboardButton(text=key,
                                              callback_data="['key', '" + value + "', '" + key + "']"))

    return markup


# вывод на экран кнопок и ввод количества обмениваемой валюты
@bot.message_handler(commands=['start','help'])
def admin_window(message):
    bot.send_message(chat_id=message.chat.id,
                     text="Выберите в первом столбце валюту, которую желаете обменять, во втором "
                          "столбце валюту, на которую желаете обменять и затем введите количество обмениваемой валюты",
                     reply_markup=makeKeyboard())

    bot.send_message(chat_id=message.chat.id, text="Введите количество меняемой валюты")
    bot.register_next_step_handler(message, convert)


# обработка выбранных кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global base, ruBase, quote, ruQuote

    if (call.data.startswith("['value'")):
        print(f"call.data : {call.data} , type : {type(call.data)}")

        base = ast.literal_eval(call.data)[1]
        ruBase = ast.literal_eval(call.data)[2]
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text="Вы кликнули " + ruBase + " и выбрали для обмена валюту " +
                                       base)



    if (call.data.startswith("['key'")):

        print(f"call.data : {call.data} , type : {type(call.data)}")

        quote = ast.literal_eval(call.data)[1]
        ruQuote = ast.literal_eval(call.data)[2]
        bot.answer_callback_query(callback_query_id=call.id,
                                  show_alert=True,
                                  text="Вы кликнули " + ruQuote + " и решили обменять на валюту " +
                                       quote)



# API запрос соотношения выбранных валют, расчет кoнвертации
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        amount = int(message.text)  # проверяем, что введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    else:
        r = requests.get(f'https://api.coingate.com/v2/rates/merchant/{base}/{quote}')
        total_base = float(r.text) * amount

        text = f'За  {amount} {ruBase} дают {total_base}  {ruQuote} '


        bot.send_message(message.chat.id, text)
#
#
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
