import requests
import xmltodict
import sys
from datetime import datetime


def currency_rates(currency=None, date=None):
    currency_codes_response = requests.get('https://www.cbr.ru/scripts/XML_valFull.asp')
    if currency_codes_response.status_code == 200:
        currency_codes_dict = xmltodict.parse(currency_codes_response.content)

        try:
            date_in_right_format = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        except ValueError:
            return 'Введите дату в формате YYYY-MM-DD'

        target_currency = None
        for i in currency_codes_dict['Valuta']['Item']:
            if i['ISO_Char_Code'] == currency:
                target_currency = i

        if target_currency is not None:
            value_response = requests.get(f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={date_in_right_format}&date_req2={date_in_right_format}&VAL_NM_RQ={target_currency['@ID']}")
            if currency_codes_response.status_code == 200:
                value_dict = xmltodict.parse(value_response.content)
                try:
                    target_value = value_dict['ValCurs']['Record']['Value']
                    return f"{target_currency['ISO_Char_Code']} ({target_currency['Name']}): {target_value}"
                except KeyError as e:
                    if e.__str__().replace('\'', '') == 'Record':
                        return 'На введенную дату нет информации'
            else:
                return 'Банк не отвечает, попробуйте позднее'
        else:
            return 'Невозможно найти введенную валюту'
    else:
        return 'Банк не отвечает, попробуйте позднее'


functions = {'currency_rates': currency_rates}

if __name__ == '__main__':
    try:
        function = [i for i in sys.argv[1:] if '--' not in i][0]
    except IndexError:
        print('Вы не указали функцию в аргументах')
        sys.exit(-1)

    try:
        currency = [i for i in sys.argv[1:] if '--code' in i][0].split('=')[1]
    except IndexError:
        print('Вы не указали необходимую валюту в аргументe --code')
        sys.exit(-1)

    try:
        date = [i for i in sys.argv[1:] if '--date' in i][0].split('=')[1]
    except IndexError:
        print('Вы не указали необходимую валюту в аргументe --date')
        sys.exit(-1)

    try:
        print(functions[function](currency, date))
    except KeyError:
        print(f'Функции "{function}" не существует')
        sys.exit(-1)
