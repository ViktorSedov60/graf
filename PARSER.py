from bs4 import BeautifulSoup
import json
import requests  # импортируем наш знакомый модуль
import telebot

"""  
Делаем кнопки в телеграмм боте
"""
responce = requests.get('https://quote.rbc.ru/')
# print(responce.text)
soup = BeautifulSoup(responce.text, "lxml")
p1 = soup.find_all('div', class_='header')
# p2 = p1.find('div', class_='js-indicators js-dragscroll')
# page = soup.find('div', class_='key-indicators__scroll')
print(p1)

# 'div' key-indicators__scroll
# 'a' title="USD, 16:51"
# 'a' key-indicators__item js-yandex-counter
# 'span' key-indicators__diff
