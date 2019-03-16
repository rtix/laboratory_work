import requests
import urllib.parse as urlparse
from urllib.request import urlopen
import time
import datetime

token = "2dcbf5142dcbf5142dcbf514db2dad8b3a22dcb2dcbf51476762a2b6d10dfdadf63a116"

def par_url(text, start_time, end_time):
    return "https://api.vk.com/method/newsfeed.search?q={0}&start_time={1}&end_time={2}&count=1&access_token={3}&v=5.92".format(text, start_time, end_time, token)

def unixtimed(date):
    return time.mktime(datetime.datetime.strptime(date, "%d-%m-%Y").timetuple())

def total_count(text, start_time, end_time):
    url = par_url(text, unixtimed(start_time), unixtimed(end_time))
    for i in range(100):
        response = requests.get(url)
        json = response.json()
        result = dict(json["response"])["total_count"]
        if result:
            break
    return dict(json["response"])["total_count"]