import requests

# API endpoint for exchange rates
url = "https://api.exchangerate-api.com/v4/latest/USD"

# Retrieve exchange rates from the API
response = requests.get(url)
exchange_rates = response.json()['rates']

# Define the function for the currency conversion
def convert_currency(amount, from_currency, to_currency):
    # Convert the amount to USD
    usd_amount = amount / exchange_rates[from_currency]
    # Convert from USD to desired currency
    converted_amount = usd_amount * exchange_rates[to_currency]

    return converted_amount

# Usage
amount = float(input("put your amount: "))
from_currency = 'USD'
to_currency = 'VES' # Only need to change this value to make an exchange
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")