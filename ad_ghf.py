# getting source html file of website
# ad_ghf = audio data _ get html file
import requests


url = 'https://publishing.linguist.ua/quickminds3/cd1/'
res = requests.get(url)
r_status = res.status_code
with open('cd1.html', 'w', encoding='utf-8') as ouf:
    if r_status == 200:
        ouf.write(res.text)
        print('File downloaded successful!')
    else:
        print('Error download')

