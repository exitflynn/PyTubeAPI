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
    rc = soup.find_all(attrs={'dir':'auto'})
    n = len(rc)
    
    vlinksoup = soup.find_all(attrs={'title':'Watch on YouTube'})
    videolinks = [RSet['href'] for RSet in vlinksoup]

    i = 0
    videocounter = 0
    dic = {}

    while i < n:
        a = rc[i]
        if str(a).find('class') == -1:
            title = rc[i].getText()
        elif str(a).find('class="channel-name"') != -1:
            channel = rc[i].getText()
        elif str(a).find('ago') != -1:
            t_upload = rc[i].getText()
        elif str(a).find('views') != -1:
            views = rc[i].getText()
            dic[videocounter] = {
                "link" : videolinks[videocounter],
                "title" : title,
                "channel" : channel,
                "upload_time" : t_upload,
                "views" : views
                }
            videocounter += 1  
        i += 1
    print(dic)
    return dic

