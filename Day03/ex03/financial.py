#!/usr/bin/env python3
import requests
import sys
import time
from bs4 import BeautifulSoup

class Financial:
    def __init__(self):
        self.ticker = None
        self.field = None

    def get_args(self):
        if len(sys.argv) != 3:
            print("Usage: ./financial.py <ticker> <field>")
            sys.exit(1)
        self.ticker = sys.argv[1].upper()
        self.field = sys.argv[2]

    def parse_yahoo_finance(self):
        url = f"https://finance.yahoo.com/quote/{self.ticker}/financials?p={self.ticker}"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Ошибка HTTP: {e}")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            sys.exit(1)

        return response.text

    def parse_financial_table(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        table_body = soup.find('div', class_='tableBody yf-9ft13')

        if not table_body:
            print("Таблица финансов не найдена.")
            return None

        data = []
        for row in table_body.find_all('div', class_='row lv-0 yf-t22klz'):
            field_name = row.find('div', class_='rowTitle yf-t22klz').text.strip()
            data_values = [col.text.strip() for col in row.find_all('div', class_='column')[1:]]
            data.append((field_name, data_values))

        return data

    def get_field_data(self, data):
        for field_name, values in data:
            if field_name == self.field:
                return values
        return None


if __name__ == "__main__":
    financial = Financial()
    financial.get_args()
    html_content = financial.parse_yahoo_finance()

    time.sleep(5)

    financial_data = financial.parse_financial_table(html_content)
    if financial_data:
        field_data = financial.get_field_data(financial_data)
        if field_data:
            print(f"{financial.field}: {field_data}")
        else:
            print(f"Поле '{financial.field}' не найдено в таблице.")
    else:
        print("Данные не взяты из таблицы.")