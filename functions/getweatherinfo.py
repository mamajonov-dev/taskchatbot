from data.config import WEATHERAPI
import requests
import json
from datetime import datetime


# функция для получения информацию о погоде, принимает название города и возвращает информацию о погоде, картинку погоды
def getweatherinfo(cityname):
    # ссылка на сайт
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': cityname,  # название города
        'appid': WEATHERAPI,  # апи пользователя
        'units': 'metric',  # Меры измерения
        'lang': 'ru'  # язык
    }
    # запрос на сайт
    response = requests.get(url, params=params)
    # помещаем входящее сообщение в переменную
    data = response.json()

    text = f"""
Название города: {data['name']}
Страна: {data['sys']['country']}
Погода: {data['weather'][0]['main']},  {data['weather'][0]['description']}
Температура: {data['main']['temp']} C˚
Ощущается как: {data['main']['feels_like']} C˚
Давление атмосферы: {data['main']['pressure']}
Влажность воздуха: {data['main']['humidity']}
Восход солнца: {datetime.fromtimestamp(data['sys']['sunrise'])}
Заход солнца: {datetime.fromtimestamp(data['sys']['sunset'])}"""
    image = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    return text, image
