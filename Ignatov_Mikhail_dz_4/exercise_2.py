import utils

currency = input('Enter currency. for example: USD: ')


print(f"{currency.upper()}: {utils.currency_rates(currency)}")
print(f"EUR: {utils.currency_rates('EUR')}")
print(f"USD: {utils.currency_rates('USD')}")