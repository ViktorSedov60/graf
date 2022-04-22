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

item = page.find('span', class_="chart__info__sum")
usd = page2.find('span', class_="chart__info__sum")
bb = item.text[1:7]
EUR = convert(bb)
print("EUR = ", EUR)


aa = usd.text[1:7]
USD = convert(aa)
print("USD = ", USD)



