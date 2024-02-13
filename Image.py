import requests
from bs4 import BeautifulSoup

web = requests.get('https://example.com')
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0

for i in imgs:
    jpg = requests.get(i['src'])
    with open(f'...\...\{name}.jpg', 'wb') as f:
        f.write(jpg.content)
    name += 1