from bs4 import BeautifulSoup
import json
import requests  # импортируем наш знакомый модуль


html = requests.get('/html/body/div[4]/div[3]/div[2]/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]')
# получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
# soup = BeautifulSoup(html, 'lxml')
# print(soup)
# попытаемся спарсить наш файл с помощью html парсера
<span class="chart__info__sum"><!--
        -->₽<!--
        --><!--
            -->77,081<!--
        -->    </span>
# ul = soup.find('/html/body/div[4]/div[3]/div[2]/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/span[1]')
# помещаем в аргумент методу findall скопированный xpath
texts1 = json.loads(html.content)
Rates1 = texts1.get('span[1]')  # убираем лишнее
EUR = str(Rates1[0])
print(EUR)
# # создаём цикл в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a') # в каждом элементе находим, где хранится заголовок новости. У нас это тег
#     # <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#     print(a.text) # из этого тега забираем текст — это и будет нашим названием