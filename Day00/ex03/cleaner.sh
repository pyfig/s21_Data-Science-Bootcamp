#!/bin/sh
# Входной CSV-файл, содержащий отсортированные данные
input_csv="hh_sorted.csv"

# Выходной CSV-файл для сохранения обработанных данных
output_csv="hh_positions.csv"

# Извлекаем заголовок и модифицируем его для нового формата
# Добавляем столбец с уровнем позиции (Junior)
header=$(head -n 1 "$input_csv" | awk -F',' '{print $1 "," $2 ",\"Junior\"," $(NF-1) "," $NF}')

# Записываем заголовок в выходной CSV-файл
echo "$header" > "$output_csv"

# Обрабатываем CSV-файл построчно
tail -n +2 "$input_csv" | while IFS= read -r line
do
  # Безопасно извлекаем поля с помощью awk
  id=$(echo "$line" | awk -F',' '{print $1}')
  created_at=$(echo "$line" | awk -F',' '{print $2}')
  name=$(echo "$line" | awk -F',' '{for (i=3; i<=NF-2; i++) printf $i ","; printf $(NF-2)}' | sed 's/,$//')
  has_test=$(echo "$line" | awk -F',' '{print $(NF-1)}')
  alternate_url=$(echo "$line" | awk -F',' '{print $NF}')

  # Извлекаем уровень позиции (Junior, Middle, Senior) и удаляем лишний текст
  # Берем только первое совпадение
  position=$(echo "$name" | grep -oE "\b(Junior|Middle|Senior)\b" | head -n 1)

  # Если уровень позиции не найден, устанавливаем значение "-"
  [ -z "$position" ] && position="-"

  # Записываем обработанную строку в выходной CSV-файл
  echo "$id,$created_at,\"$position\",$has_test,$alternate_url" >> "$output_csv"
done

echo "Обработка завершена. Обработанный CSV-файл сохранен как $output_csv."
