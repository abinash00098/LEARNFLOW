# currency_converter.py
from exchange_rates import fetch_exchange_rates

def convert_currency(amount, from_currency, to_currency):
    rates = fetch_exchange_rates()
    
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code")
    
    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    
    return converted_amount

if __name__ == "__main__":
    # Example usage
    amount = 100
    from_currency = 'USD'
    to_currency = 'EUR'
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
