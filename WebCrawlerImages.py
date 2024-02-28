from requests import get
from bs4 import BeautifulSoup

url = 'https://github.com'
web = get(url)
soup = BeautifulSoup(web.text, 'html.parser')
imgs = soup.find_all('img')
number = 0

for i in imgs:
    jpg = get(i['src'])
    with open(f'.\\{number}.jpg', 'wb') as f:
        f.write(jpg.content)
    number += 1