# exchange_rates.py
import requests

API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'  # Example API endpoint

def fetch_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data['rates']

if __name__ == "__main__":
    rates = fetch_exchange_rates()
    print(rates)
