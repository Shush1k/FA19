import requests
import datetime
import locale
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
locale.setlocale(locale.LC_ALL, "")


def get_html(url):                                                          # Получение html страницы
    if url:
        r = requests.get(url, headers={'User-Agent': UserAgent().chrome})
        html = r.text
        return html


def parser(html, repertuar):
    data_theatre = {}
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('ul', class_='list-group')                            # Таблица html кода
    #print(table)
    blocks = table.find_all('li', class_='list-group-item')                 # Блок со списком событий
    for i in range(len(blocks)):
        date = blocks[i].find('span', class_='date')
        date = str(date.text).strip()
        try:                                                                # Високосный год
            check_date = datetime.datetime.strptime(date, '%d %b %H:%M')
        except ValueError:
            check_date = date + ' 2020'
            check_date = datetime.datetime.strptime(check_date, '%d %b %H:%M %Y')
            if check_date.month == 4 or check_date.month == 3 or \
                    check_date.month == 2 or check_date.month == 1:
                date = date + ' 2020'
            else:
                date = date + ' 2019'
        else:
            if check_date.month == 4 or check_date.month == 3 or \
                    check_date.month == 2 or check_date.month == 1:
                date = date + ' 2020'
            else:
                date = date + ' 2019'
        date = datetime.datetime.strptime(date, '%d %b %H:%M %Y')           # Дата и время

        block = blocks[i].find('div', class_='left_block')
        name = block.find('a', class_='show_name')
        about = name.get('href')
        about = 'https://bilety-teatr.ru' + about                           # Описание
        name = str(name.text).strip()                                       # Название

        image = blocks[i].find_all('div')
        image = image[0].find('img')
        image = image.get('src')
        if image:
            image = 'https://bilety-teatr.ru' + image
        else:
            image = None                                                    # Картинка

        where = block.find('div', class_='where')
        link_where = None
        if repertuar:
            link_where = where.find('a').get('href')
            link_where = 'https://bilety-teatr.ru' + link_where             # Театр
        where = str(where.text).strip()
        if not repertuar:
            where = where.split()
            if len(where) > 2:
                where = ' '.join(where[0:2])
            else:
                where = ' '.join(where)                                     # Сцена

        block = blocks[i].find('div', class_='right_block')
        count = None
        price = None
        buy = None
        if block:
            tickets = block.find('div', class_='how_many_tckts')
            if tickets:
                tickets = str(tickets.text).strip()
                tickets = tickets.split()
                count = ' '.join(tickets[0:2])                              # Кол-во билетов
                price = ' '.join(tickets[2:])                               # Цена
                buy = block.find('a', class_='btn btn-sm btn--danger')
                buy = buy.get('href')
                buy = 'https://bilety-teatr.ru' + buy                       # Купить

        data_theatre[i] = {
            'date': date, 'name': name, 'about': about, 'image': image,
            'where': where, 'count': count, 'price': price, 'buy': buy,
            'link_where': link_where
        }
    return data_theatre


def get_pushkin():
    url = 'https://bilety-teatr.ru/repertuar/teatr-pushkina/'
    data = parser(get_html(url), False)
    return data


def get_chehov():
    url = 'https://bilety-teatr.ru/repertuar/mht-chehova/'
    data = parser(get_html(url), False)
    return data


def get_mayakovski():
    url = 'https://bilety-teatr.ru/repertuar/teatr-mayakovskogo/'
    data = parser(get_html(url), False)
    return data


def get_small():
    url = 'https://bilety-teatr.ru/repertuar/malyi-teatr/'
    data = parser(get_html(url), False)
    return data


def get_big():
    url = 'https://bilety-teatr.ru/repertuar/bolshoy-teatr/'
    data = parser(get_html(url), False)
    return data


def get_bulgakov():
    url = 'https://bilety-teatr.ru/repertuar/teatr-bulgakova/'
    data = parser(get_html(url), False)
    return data


def get_gogol():
    url = 'https://bilety-teatr.ru/repertuar/teatr-gogol/'
    data = parser(get_html(url), False)
    return data


def get_stanislavski():
    url = 'https://bilety-teatr.ru/repertuar/elektroteatr-stanislavskogo/'
    data = parser(get_html(url), False)
    return data


def get_gorki():
    url = 'https://bilety-teatr.ru/repertuar/mhat-im-gorkogo/'
    data = parser(get_html(url), False)
    return data


def get_repertuar(date):
    date = date.strftime('%d %m %Y')
    date = str(date).split()
    url = 'https://bilety-teatr.ru/repertuar/' + f'date/{date[2]}/{date[1]}/{date[0]}/'
    data = parser(get_html(url), True)
    return data


if __name__ == '__main__':
    print(get_repertuar(datetime.datetime(2019, 12, 26).date()))
