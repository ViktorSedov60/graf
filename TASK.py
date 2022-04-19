# # int_list = []
# # for element in input("ведите любые целые числа в любом количестве через пробел.").split():
# #     int_list.append(int(element))
# # s = sorted(int_list)
# # print(s)
#
#
# s = "5 6 11 13 2 3 14 1 9 15 10 8 7 6"
# n = (sorted(list(map(int, s.split()))))
# print(n)
# M = max(n)
# V = min(n)
#
#
#
# def get_01 ():
#     while True:
#         get_1 = input('Введите целое положительное число в пределах списка: ')  # Ввод числа
#         if get_1.isdigit():
#             return get_1
# A = int(get_01())
#
#
# def get_2 (n, A):
#     for i in range(len(n)):
#         if A >= n[i] and A <= n[i + 1]:
#             return i
#
#
# if V > A:
#     print(" Введено число меньше минимального списка")
#     A = int(get_01())
# elif V == A:
#     print("Введено число равное минимальному в списке")
#
# elif M == A:
#     print("введено число равное максимальному в списке")
# elif V < A < M:
#     print("Введено число в пределах списка ")
#
# elif A > M:
#     print("Введено число больше максимального в списке ")
#     A = int(get_01())
#
# position = get_2(n, A)
#
# print("нидекс= ", position)



import telebot

TOKEN = "5388915598:AAHpezc8UkpCIPIPJzmbwwhU4MqzN4SZCL8"

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler( commands=['start','help'])
# def handle_start_help(message):
#     pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Welcome, {message.chat.username}")


# Обрабатываются все голосовые сообщения
@bot.message_handler(content_types=['voice',])
def repeat(message: telebot.types.Message):
    bot. send_message(message.chat.id, f"у  тебя, {message.chat.username} , красивый голос!")


# обрабатываются сообщения, содержащие фото
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


@bot.message_handler(commands=['start'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')

bot.polling(none_stop=True)