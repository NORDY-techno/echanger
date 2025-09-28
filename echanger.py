'''
ввід валюти тільки в грн
конвертується тільки у USD,EUR
якщо щось неправильно то виведе "помилка"
'''

exchange_rates = {
    "EUR": 48.22000,
    "USD": 41.10000
}
uah = float(input("Введіть суму : "))
currency = input("В яку валюту конвертувати (EUR або USD): ").upper()
if currency in exchange_rates:
    result = uah / exchange_rates[currency]
    print(uah, "грн =", round(result, 2), currency)
else:
    print("помилка")

