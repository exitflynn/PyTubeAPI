import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI, Path

pyt = FastAPI()

@pyt.get("/{search_term}")
def get_info(search_term: str):
    return main(search_term)

def main(search_term):
    resp = requests.get(f"https://vid.puffyan.us/search?q={search_term}")
    txt = resp.text

    soup = BeautifulSoup(txt, "html.parser")
    l = soup.find_all(attrs={'dir':'auto'})
    n = len(l)

    i = 0
    m = 0
    dic = {}

    while i < n:
        a = l[i]
        if str(a).find('class') == -1:
            title = l[i].getText()
        elif str(a).find('class="channel-name"') != -1:
            channel = l[i].getText()
        elif str(a).find('ago') != -1:
            t_upload = l[i].getText()
        elif str(a).find('views') != -1:
            views = l[i].getText()
            dic[m] = {
                "title" : title,
                "channel" : channel,
                "upload_time" : t_upload,
                "views" : views
                }
            m += 1  
        i += 1
    print(dic)
    return dic

