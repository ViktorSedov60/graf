import re

import requests
import bs4

def convert(num):
    i = float(num.replace(",", "."))
    return i


responce = requests.get('https://quote.rbc.ru/ticker/59090')
html = requests.get('https://quote.rbc.ru/ticker/72413')

# print(responce.status_code)
# print(html.status_code)

page = bs4.BeautifulSoup(responce.text, 'lxml')
page2 = bs4.BeautifulSoup(html.text, 'lxml')

eur = page.find('span', class_="chart__info__sum").text[1:7]
# item = page.find('span', text=re.compile('EUR')).text

usd = page2.find('span', class_="chart__info__sum").text[1:7]


EUR = convert(eur)
print("EUR = ", EUR)

USD = convert(usd)
print("USD = ", USD)



