import requests
from bs4 import BeautifulSoup

resp = requests.get("https://vid.puffyan.us/search?q=pokemon")
txt = resp.text

soup = BeautifulSoup(txt, "html.parser")
l = soup.find_all(attrs={'dir':'auto'})
n = len(l)

i = 0
while i < n:
    # try:
    #     if l[i]['class'][0] == 'channel-name':
    #         print(' | ',l[i].getText())
    #     i += 1
    # except:
    #     try:
    #         if l[i]['class'][0] == 'video-data':
    #             print(' - ', l[i].getText())
    #         i+=1
    #     except:
    #         i+=1
    a = l[i]
    if str(a).find('class="channel-name"') != -1:
        print(' |', l[i].getText())
        i += 1
    else if str(a).find('class="video-data"') != -1:
        print(' - ', l[i].getText())
    else:
        print("\n ", ;[i].getText())
    i += 1

# print(l[145]['class'][0])
# print(l[145])
# if l[145]['class'][0]=='channel-name':
#     print(l[145].getText())
