import requests
import decimal
import datetime

def currency_rates(argv):
    if len(argv) > 1:
        program, currency = argv
        currency = currency.upper()
        resp_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        if currency not in resp_text:
            return None
        result = resp_text[resp_text.find('<Value>', resp_text.find(currency)) + 7:resp_text.find('</Value>', resp_text.find(currency))]
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

        return (f'{decimal.Decimal(result.replace(",", ".")):.2f}, {date_result}')
    else:
        return 0


if __name__ == '__main__':
   import sys

   exit(currency_rates(sys.argv))