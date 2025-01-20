from requests import get
from bs4 import BeautifulSoup
from os import path, mkdir

def web_crawler_images(url: str, images_path: str):
    web = get(url)
    soup = BeautifulSoup(web.text, 'html.parser')
    imgs = soup.find_all('img')
    number = 1

    if not path.exists(images_path):
        mkdir(images_path)

    for i in imgs:
        jpg = get(i['src'])
        with open(f'{images_path}/{number}.jpg', 'wb') as f:
            f.write(jpg.content)
        number += 1
