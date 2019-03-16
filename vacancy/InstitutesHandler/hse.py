#!/usr/bin/env python

# {'title':str, 'salary':str, 'url':str}

import requests
import re

from bs4 import BeautifulSoup


def __func(url, arr):
    session = requests.sessions.Session()
    session.headers.update(
        {"User-Agent": "Mozilla/5.0 (X11; Linux 5.0.2-arch1-1-ARCH x86_64; Russian) KHTML/5.56.0 (like Gecko) Konqueror/5 KIO/5.56"}
    )
    soup = BeautifulSoup(session.get(url).text, "html.parser")

    try:
        next_page = soup.find_all("a", {"class": "HH-Pager-Controls-Next"})[0]['href']
    except IndexError:
        next_page = None

    vacancies_ = soup.find_all("div", {"class": "vacancy-serp-item"})
    for vacancy in vacancies_:
        vac = {}
        needed_info = vacancy.find_all("div", {"class": "vacancy-serp-item__row"})[0]
        name_url = needed_info.find("a", {"class": "bloko-link HH-LinkModifier"})
        vac["url"] = re.sub(r'//(\w+\.)', '//', name_url["href"].split("?query=")[0])
        vac["title"] = name_url.text
        try:
            vac["salary"] = needed_info.find("div", {"class": "vacancy-serp-item__compensation"}).text.replace(u"\xa0", '')
        except AttributeError:
            vac["salary"] = ""
        arr.append(vac)

    if next_page:
        __func("https://hh.ru" + next_page, arr)


def get_vacancy():
    url = ("https://hh.ru/search/vacancy?"
       "text=Национальный+исследовательский+университет+«Высшая+школа+экономики»&search_period=30&items_on_page=100"
       )
    vacancies = []
    __func(url, vacancies)
    return vacancies

