# {'title':str, 'salary':str, 'url':str}
import requests
from bs4 import BeautifulSoup


def get_vacancy():
    url = r"https://university.innopolis.ru/about/job/"

    vacancy_class = r"panel panel-default"
    title_class = r"accordion-toggle"
    salary_class = r"pull-right"
    url_class = r"btn btn-color-1"

    result = []
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    vacancy = soup.find_all('div', {'class':vacancy_class})
    for vac in vacancy:
        result_item = {}
        result_item['title'] = vac.find('a', 
                                        {'class':title_class}).string.strip()
        result_item['salary'] = vac.find('p', 
                                        {'class':salary_class}).string.strip()
        if result_item['salary']==r'з/п не указана':
            result_item['salary'] = None
        result_item['url'] = vac.find('a', {'class':url_class})["href"]
        result.append(result_item)
    return result