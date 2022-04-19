from bs4 import BeautifulSoup

import requests  # импортируем наш знакомый модуль


html = requests.get('https://www.python.org/').content
# получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
soup = BeautifulSoup(html, 'lxml')
# попытаемся спарсить наш файл с помощью html парсера

ul = soup.findall('/html/body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')
# помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a') # в каждом элементе находим, где хранится заголовок новости. У нас это тег
    # <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    print(a.text) # из этого тега забираем текст — это и будет нашим названием