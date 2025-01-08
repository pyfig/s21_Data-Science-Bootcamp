import sys

def company_dict():
    return {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

def stock_dict():
    return {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

def ticker_symbols():
    companies = company_dict()
    stocks = stock_dict()
    if len(sys.argv) == 2:
        ticker = sys.argv[1].upper()
        ticker_to_company = {v: k for k, v in companies.items()}
        if ticker in stocks:
            print(f"{ticker_to_company[ticker]} {stocks[ticker]}")
        else:
            print("Unknown ticker")

if __name__ == '__main__':
    ticker_symbols()

