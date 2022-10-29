from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS


URL = 'https://doramy.club/strana/yuzhnaya-koreya'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='post-home')
    doramy = []
    for item in items:
        info = item.find('tbody', class_='tbody-hom').getText().replace(',', '')
        sim = ['Сериал:', 'Страна:', 'Год:', 'Жанр:', '\n']
        for i in sim:
            info = info.replace(i, ', ')
        info = info.split(', ')
        doramy.append({
            'title': item.find('a').getText(),
            'link': item.find('a').get('href'),
            'series': info[-4],
            'country': info[-3],
            'year': info[-2],
            'genre': info[-1],
            'status': item.find('div', class_='status').getText()
            if item.find('div', class_='status') is not None else 'Завершён'
        })
    # pprint (doramy)
    return doramy


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        dramas = []
        for page in range(2, 3):
            html = get_html(f'{URL}/page/{page}/')
            current_page = get_data(html.text)
            dramas.extend(current_page)
        return dramas
    else:
        raise Exception('Error is parser')

# html = get_html(URL)
# get_data(html.text)