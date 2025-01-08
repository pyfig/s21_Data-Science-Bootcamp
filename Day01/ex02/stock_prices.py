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

def stock_prices():
    companies = company_dict()
    stocks = stock_dict()
    if len(sys.argv) == 2:
        company = sys.argv[1].capitalize()
        if company in companies:
            print(stocks[companies[company]])
        else:
            print("Unknown company")

if __name__ == '__main__':
    stock_prices()
