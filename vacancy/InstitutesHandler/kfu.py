# {'title':str, 'salary':str, 'url':str}
import requests
import re
from bs4 import BeautifulSoup

vacancy=[]
def get_all_vacancy(url):
    bs=BeautifulSoup(requests.get(url).text,'html.parser')
    url1="https://career.kpfu.ru"

    vac=bs.findAll('div',{'class':'vacancyItem header'})
    for i in vac:
        res={}
        res['title']=i.find('div',{'class':'vacancyItem-name'}).text
        res['salary']=i.find(text=re.compile(r'от \d{1,9}.*'))
        if res['salary'] == 'Не указано':
            res['salary'] = ""
        res['url']=url1+i.find('div',{'class':'vacancyItem-name'}).find('a')['href']
        vacancy.append(res)
    if(bs.find('a',title="На следующую страницу")):
        return get_all_vacancy(url+bs.find('a',title="На следующую страницу").attrs['href'])
    return vacancy
def get_vacancy():
    return get_all_vacancy("https://career.kpfu.ru/vacancy/kfu")