import requests
import decimal
import datetime
import json

def currency_rates(currency):

    """смотрим курс рубля и плачем"""
    # решает вопрос ввода нижним регистром
    currency = currency.upper()
    # превращаем все что есть на сайте в строку
    resp_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    #на случай если валюты нет
    if currency not in resp_text:
        return None
    # ищем в строке вЭлью нужной валюты
    result = resp_text[resp_text.find('<Value>', resp_text.find(currency)) + 7:resp_text.find('</Value>', resp_text.find(currency))]
    # проблемы со временем
    time = response.headers['Date']
    list_1 = time.split()
    dict_1 = {'Jan': '01',
              'Feb': '02',
              'Mar': '03',
              'Apr': '04',
              'May': '05',
              'Jun': '06',
              'Jul': '07',
              'Aug': '08',
              'Sep': '09',
              'Oct': '10',
              'Nov': '11',
              'Dec': '12'}
    date_result = datetime.date(int(list_1[3]), int(dict_1[list_1[2]]), int(list_1[1]))
    return f'{decimal.Decimal(result.replace(",", ".")):.2f}, {date_result}'


