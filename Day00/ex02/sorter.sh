#!/bin/sh

# Входной CSV-файл, содержащий данные о вакансиях
input_csv="hh.csv"
# Выходной CSV-файл, который будет содержать отсортированные данные
output_csv="hh_sorted.csv"

# Сохраняем заголовок из входного файла
header=$(head -n 1 $input_csv)

# Сортируем данные по дате (столбец 2), затем по ID (столбец 1)
# -t, устанавливает запятую как разделитель полей
# -k2,2 сортирует по дате
# -k1,1 сортирует по ID 
tail -n +2 $input_csv | sort -t, -k2,2 -k1,1 > $output_csv

# Добавляем заголовок обратно в начало отсортированного файла
# Создаем временный файл с заголовком + отсортированными данными, затем заменяем выходной файл
echo "$header" | cat - $output_csv > temp && mv temp $output_csv

# Выводим сообщение о завершении
echo "Сортировка завершена. Отсортированный CSV-файл сохранен как $output_csv."
