from requests import get
from datetime import date
from decimal import Decimal


def currency_rates(currency_to_exchange: str):
    """
    gets currency rate to RUR from cbr and print it.
    :param currency_to_exchange: 3-symbols sting formated "CUR"
    :return: string formated "At yyyy-mm-dd X CUR is Y RUR"
    """

    response = get("http://www.cbr.ru/scripts/XML_daily.asp").text
    # получаем индекс текущей даты
    date_index = response.find('ValCurs Date="') + len('ValCurs Date="')
    day, month, year = (int(x) for x in response[date_index:date_index+len("dd.mm.yyyy")].split("."))
    current_date = date(year, month, day)

    # получаем индекс необходимой валюты
    currency_index = response.find(currency_to_exchange.upper())
    if currency_index == -1:
        return None
    # срезаем response, чтобы следующие Nominal и Value относились к данной валюте
    sliced_response = response[currency_index:]

    # находим начало и конец данных о Nominal, получаем величину
    nominal_start_index = sliced_response.find("<Nominal>") + len("<Nominal>")
    nominal_end_index = sliced_response.find("</Nominal>")
    nominal = sliced_response[nominal_start_index:nominal_end_index]

    # находим начало и конец данных о Value, получаем величину
    rate_start_index = sliced_response.find("<Value>") + len("<Value>")
    rate_end_index = sliced_response.find("</Value>")
    rate = sliced_response[rate_start_index:rate_end_index]
    rate = rate.replace(",", ".")

    return f"At {current_date} {nominal} {currency_to_exchange.upper()} is {Decimal(rate)} RUR"


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        _module_name, input_currency = sys.argv
        exit(print(currency_rates(input_currency)))
    else:
        exit(print(currency_rates("USD")))
