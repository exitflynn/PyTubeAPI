import requests
from bs4 import BeautifulSoup

def main(search_term):
    resp = requests.get(f"https://vid.puffyan.us/search?q={search_term}")
    txt = resp.text

    soup = BeautifulSoup(txt, "html.parser")
    l = soup.find_all(attrs={'dir':'auto'})
    n = len(l)

    i = 0
    while i < n:
        a = l[i]
        if str(a).find('class') == -1:
            print("\n ", l[i].getText())
        elif str(a).find('class="channel-name"') != -1:
            print(' |', l[i].getText())
        elif (str(a).find('class="video-data"') != -1):
            print(' - ', l[i].getText())
        i += 1
main('pokemon')
    
