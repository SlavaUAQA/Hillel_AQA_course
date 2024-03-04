import datetime
import requests

class CurrencyExchange:
    def get_api(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
        response = requests.get(url)
        return response.json()

    def convert_currency_rate(self, response):
        currency_convert = ""
        for number, currency in enumerate(response, start=1):
            currency_convert += f"{number}. {currency['txt']} to UAH: {currency['rate']}\n"
        return currency_convert

    def save_currency_rate(self, response, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{datetime.date.today()}\n\n")
            file.write(self.convert_currency_rate(response))
            
currency_exchange = CurrencyExchange()
data = currency_exchange.get_api()
currency_exchange.save_currency_rate(data, "currency_rate.txt")
