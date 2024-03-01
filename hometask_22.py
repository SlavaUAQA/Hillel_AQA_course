import datetime

import requests


class CurrencyExchange:
    def get_api(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
        response = requests.get(url)
        return response.json()

    def save_currency_rate(self, response, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{datetime.date.today()}\n\n")
            for number, currency in enumerate(response, start=1):
                file.write(f"{number}. {currency['txt']} to UAH: {currency['rate']}\n")


currency_exchange = CurrencyExchange()
data = currency_exchange.get_api()
currency_exchange.save_currency_rate(data, "currency_rate.txt")
