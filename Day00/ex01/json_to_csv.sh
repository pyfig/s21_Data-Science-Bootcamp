#!/bin/bash

# Входной JSON-файл, содержащий данные о вакансиях
input_json="hh.json"

# Выходной CSV-файл, в который будут записаны преобразованные данные
output_csv="hh.csv"

# Файл с JQ-фильтром для обработки JSON
filter_file="filter.jq"

# Используем jq для преобразования JSON в CSV:
# -r выводит "сырые" строки без кавычек
# -f загружает фильтр из файла
# Извлекаем нужные поля (id, created_at, name, has_test, alternate_url) и форматируем их как CSV
jq -r -f $filter_file $input_json | jq -r '[.id, .created_at, .name, .has_test, .alternate_url] | @csv' > $output_csv

# Выводим сообщение об успешном завершении
echo "Конвертация завершена. CSV файл сохранен как $output_csv."
