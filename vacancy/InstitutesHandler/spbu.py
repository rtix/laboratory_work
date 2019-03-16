# {'title':str, 'salary':str, 'url':str}
import requests
from bs4 import BeautifulSoup


def get_vacancy():
    url = r"http://hr.spbu.ru/vacansii.html"
    vac_url = url[:-5]

    result = []
    r = requests.post(url, data={'limit':0})
    soup = BeautifulSoup(r.text, 'html.parser')
    vacancy = soup.find_all('td')
    for vac in vacancy:
        result_item = {}
        result_item['title'] = vac.find('a').string.strip()
        result_item['salary'] = ""
        result_item['url'] = vac_url + vac.find('a')["href"].split("-")[0]
        result.append(result_item)
    return result