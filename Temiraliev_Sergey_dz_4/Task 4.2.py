import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    """ Функция, используя код валюты, показывает курс валюты с сайта ЦБ РФ"""

    if not (currency_code and url):
        return None

    currency_code = currency_code.upper()  # перевод введенного кода валюты в вверхний регистр
    respond = requests.get(url)

    if respond.ok:
        # разделение строки по введённому коду валюты. Получаем список из двух элементов
        cur = respond.text.split(currency_code)

        # проверка на корректность введенного кода валюты. len(cur) должно быть равно 2
        if len(cur) == 1:
            print('Вы неправильно ввели код валюты')
            return None
        # получение параметров валюты: название, номинал, стоимость в рублях
        currency_name = cur[1].split("</Name>")[0].split("<Name>")[1]
        currency_nominal = cur[1].split("</Nominal>")[0].split("<Nominal>")[1]
        value = cur[1].split("</Value>")[0].split("<Value>")[1]

        # перевод стоимости value из str в float
        currency_value = float(value.replace(",", "."))

        # получение даты с сервера сайта
        date = respond.headers['Date']

        print(f'Курс {currency_code} на сегодня ({date}):\n'
              f'{currency_nominal} {currency_name} составляет {currency_value} Российских рублей')

    else:
        return None


currency = str(input('Введите код валюты: '))
currency_rates(currency)
