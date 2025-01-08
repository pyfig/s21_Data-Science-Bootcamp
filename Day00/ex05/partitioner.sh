#!/bin/sh

INPUT_FILE="hh_positions.csv"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Input file '$INPUT_FILE' not found."
    exit 1
fi

header=$(head -n 1 "$INPUT_FILE")

awk -F',' 'NR > 1 {gsub("\"", "", $2); split($2, date, "T"); print date[1]}' "$INPUT_FILE" | sort -u | while read -r date; do
    [ -z "$date" ] && continue
    
    output_file="${date}.csv"
    
    echo "$header" > "$output_file"
    
    awk -F',' -v date="$date" -v OFS=',' 'NR > 1 {gsub("\"", "", $2); if ($2 ~ date) print}' "$INPUT_FILE" | sort -u >> "$output_file"
    echo "Created file: $output_file"
done