#!/bin/sh

OUTPUT_FILE="concatenated.csv"

> "$OUTPUT_FILE"

for file in *.csv; do
    if [ "$file" != "$OUTPUT_FILE" ]; then
        head -n 1 "$file" > "$OUTPUT_FILE"
        break
    fi
done

for file in *.csv; do
    if [ "$file" != "$OUTPUT_FILE" ]; then
        tail -n +2 "$file" | sed 's/"//g'
    fi
done | sort -u >> "$OUTPUT_FILE"

echo "Комбо вомбо файл готов: $OUTPUT_FILE"