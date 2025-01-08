#!/usr/bin/env python3

import pytest
import httpx
from bs4 import BeautifulSoup
from financial_enhanced import Financial

class TestFinancial:
    @pytest.fixture
    def financial(self):
        financial = Financial()
        financial.ticker = "MSFT"  
        financial.field = "Total Revenue"  
        return financial

    def test_total_revenue_valid_ticker(self, mocker, financial):
        mock_response = mocker.Mock()
        mock_response.text = """
            <html>
                <div class='tableBody yf-9ft13'>
                    <div class='row lv-0 yf-t22klz'>
                        <div class='rowTitle yf-t22klz'>Total Revenue</div>
                        <div class='column'>254,190,000</div> 
                        <div class='column'>245,122,000</div> 
                        <div class='column'>211,915,000</div> 
                        <div class='column'>198,270,000</div> 
                        <div class='column'>168,088,000</div> 
                    </div>
                </div>
            </html>
        """
        mock_response.status_code = 200
        mock_response.raise_for_status = lambda: None

        mocker.patch("httpx.get", return_value=mock_response)

        html_content = financial.parse_yahoo_finance()
        financial_data = financial.parse_financial_table(html_content)
        result = financial.get_field_data(financial_data)

        # Extract all values from the first row of the table
        expected_values = [col.text.strip() for col in 
                           BeautifulSoup(mock_response.text, 'html.parser')
                           .find('div', class_='tableBody yf-9ft13')
                           .find('div', class_='row lv-0 yf-t22klz')
                           .find_all('div', class_='column')[1:]]

        assert result == expected_values, "Возращает Total Revenue значения"


    def test_return_type_is_list_of_tuples(self, mocker, financial):
        mock_response = mocker.Mock()
        mock_response.text = """
            <html>
                <div class='tableBody yf-9ft13'>
                    <div class='row lv-0 yf-t22klz'>
                        <div class='rowTitle yf-t22klz'>Total Revenue</div>
                        <div class='column'>12345</div>
                    </div>
                </div>
            </html>
        """
        mock_response.status_code = 200
        mock_response.raise_for_status = lambda: None
        
        mocker.patch("httpx.get", return_value=mock_response)
        
        html_content = financial.parse_yahoo_finance()
        financial_data = financial.parse_financial_table(html_content)
        
        assert isinstance(financial_data, list), "Возращает список"
        assert len(financial_data) > 0, "Проверка на пустой список"
        assert all(isinstance(item, tuple) for item in financial_data), "Каждый элемент списка - кортеж"
        assert len(financial_data[0]) == 2, "Каждый кортеж состоит из двух элементов"

    def test_invalid_ticker_raises_exception(self, mocker, financial):
        mocker.patch("httpx.get", side_effect=httpx.HTTPStatusError(
            "404 Not Found",
            request=mocker.Mock(),
            response=mocker.Mock(status_code=404)
        ))
        
        with pytest.raises(SystemExit):
            financial.parse_yahoo_finance()

    def test_field_not_found(self, mocker, financial):
        mock_response = mocker.Mock()
        mock_response.text = """
            <html>
                <div class='tableBody yf-9ft13'>
                    <div class='row lv-0 yf-t22klz'>
                        <div class='rowTitle yf-t22klz'>Different Field</div>
                        <div class='column'>12345</div>
                    </div>
                </div>
            </html>
        """
        mock_response.status_code = 200
        mock_response.raise_for_status = lambda: None
        
        mocker.patch("httpx.get", return_value=mock_response)
        
        html_content = financial.parse_yahoo_finance()
        financial_data = financial.parse_financial_table(html_content)
        result = financial.get_field_data(financial_data)
        
        assert result is None, "Возращает None для несуществующего поля"
