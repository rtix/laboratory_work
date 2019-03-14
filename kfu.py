# {'title':str, 'salary':str, 'url':str}
import requests
import re
from bs4 import BeautifulSoup


def get_vacancy():
    url="https://career.kpfu.ru/vacancy/kfu"
    bs=BeautifulSoup(requests.get(url).text,'html.parser')
    url1="https://career.kpfu.ru"
    vacancy=[]

    vac=bs.findAll('div',{'class':'vacancyItem header'})
    for i in vac:
        res={}
        res['title']=i.find('div',{'class':'vacancyItem-name'}).text
        res['salary']=i.find(text=re.compile(r'от \d{1,9}.*'))
        res['url']=url1+i.find('div',{'class':'vacancyItem-name'}).find('a')['href']
        vacancy.append(res)
        #РАдиф, все хорошо,не волнуйся.пше
    return vacancy
print(get_vacancy())