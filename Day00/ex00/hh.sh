#!/bin/bash

# Hardcoded search vacancy xd
SEARCH_VACANCY='data+scientist'

# API URL headhunter'a for searching vacancies with $SEARCH_TERM
API_URL="https://api.hh.ru/vacancies?text=$SEARCH_VACANCY&per_page=20"

# Use curl to fetch data from the API and jq to format it into a readable JSON
curl -s "$API_URL" | jq '.' > hh.json

# Success ?
echo "Список вакансий сохранен в hh.json"
