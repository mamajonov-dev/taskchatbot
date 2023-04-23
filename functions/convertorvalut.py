from data.config import EXCHANGERATESAPI
import requests
from pprint import pprint as print
import json
from datetime import datetime


# функция для получения конвертации валют
def get_currency(from_, to_, amount):  # принимает 3 параметра

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount}"
    payload = {}
    headers = {
        "apikey": EXCHANGERATESAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    if status_code == 200:
        data = response.json()
        fromval = data['query']['from']
        toval = data['query']['to']
        amount = data['query']['amount']
        timecurrrency = datetime.fromtimestamp(data['info']['timestamp'])
        result = data['result']
        text = f'Откуда: {fromval}\n' \
               f'Куда: {toval}\n' \
               f'Конвертируемая сумма: {amount}\n' \
               f'Резултат: {result} {toval}\n\n' \
               f'Время конвертации: {timecurrrency}\n'
        return text
    else:
        return 'Некорректный формат'


# функция для получения символы валют
def getcurrencysmybols():
    url = f"https://api.apilayer.com/exchangerates_data/symbols"
    payload = {}
    headers = {
        "apikey": EXCHANGERATESAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    return result
