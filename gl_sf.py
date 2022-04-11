# getting links to mp3files and saving mp3
# gl_sf = get links _ save files
import requests
from bs4 import BeautifulSoup

with open('cd1.html', 'r', encoding='utf-8-sig') as inf:
    text = inf.read()

# getting list of links to mp3 files
soup = BeautifulSoup(text, 'lxml')
ts = soup.select('source[src]')
links_list = [el['src'] for el in ts]

# downloading mp3 files to current folder
for num in range(len(links_list)):
    res = requests.get(links_list[num])
    if res.status_code == requests.codes.ok:
        with open(f'track{num + 1}.mp3', 'wb') as ouf:
            ouf.write(res.content)
        print(f"Track {num + 1} downloaded successfully!")
    else:
        print(f'Download ERROR, status code: {res.status_code}')
