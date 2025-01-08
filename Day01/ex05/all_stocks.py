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

def process_expression(expression, companies, stocks):
    expression = expression.strip().capitalize()
    if expression in companies:
        ticker = companies[expression]
        return f"{expression} stock price is {stocks[ticker]}"
    elif expression.upper() in stocks:
        company = [name for name, symbol in companies.items() if symbol == expression.upper()]
        if company:
            return f"{expression.upper()} is a ticker symbol for {company[0]}"
    return f"{expression} is an unknown company or an unknown ticker symbol"

def all_stocks():
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]
    if ',,' in input_string:
        return

    companies = company_dict()
    stocks = stock_dict()

    expressions = input_string.split(',')
    for expression in expressions:
        expression = expression.strip()
        if expression:
            result = process_expression(expression, companies, stocks)
            print(result)

if __name__ == '__main__':
    all_stocks()
