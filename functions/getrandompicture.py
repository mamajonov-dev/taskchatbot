import random
import requests
import json
from data.config import PIXBAYANIMALS


#  Функция для отправки случайной картинки с милыми животными
def getcuteanimals():
    # ссылка на сайт
    url = f"https://pixabay.com/api/?key={PIXBAYANIMALS}&q=animal&image_type=photo"
    # запрос на сайт
    response = requests.get(url)
    # помещаем входящее сообщение в переменную
    data = response.json()
    links = []
    for link in data['hits']:
        image = link['pageURL']
        links.append(image)
    return random.choice(links)  # возвращает случайную картинку
