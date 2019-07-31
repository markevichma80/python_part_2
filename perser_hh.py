import requests
from lxml import html

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
langvich = input('введите язык програмирования для поиска:')
base_url = 'https://hh.ru/search/vacancy'


def pars_hh(base_url, params, headers):
    try:
        req = requests.get(base_url, params=params, headers=headers)
        root = html.fromstring(req.text)
        list_p = root.xpath("//div[@class='vacancy-serp-item__row vacancy-serp-item__row_header']")
        for i in list_p:
            print(i.xpath(".//a/text()")[0], i.xpath(".//a/@href")[0])
            try:
                print(i.xpath(".//div[contains(@class, 'vacancy-serp-item__compensation')]/text()")[0])
            except IndexError:
                print('не указанно')
            print('=' * 25)
    except requests.exceptions.ConnectionError:
        print("No connection to site")


for page in range(2):
    params = {
        'search_period': 3,
        'text': f'Програмист {langvich}',
        'page': page
    }
    pars_hh(base_url, params, headers)
