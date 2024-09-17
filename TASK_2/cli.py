# cli.py
import argparse
from currency_converter import convert_currency

def main():
    parser = argparse.ArgumentParser(description="Currency Converter CLI")
    parser.add_argument('amount', type=float, help="Amount to convert")
    parser.add_argument('from_currency', type=str, help="Currency code to convert from")
    parser.add_argument('to_currency', type=str, help="Currency code to convert to")
    
    args = parser.parse_args()
    
    try:
        result = convert_currency(args.amount, args.from_currency, args.to_currency)
        print(f"{args.amount} {args.from_currency} = {result:.2f} {args.to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
