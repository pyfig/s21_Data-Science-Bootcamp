#!/bin/sh

INPUT_FILE="hh_positions.csv"
OUTPUT_FILE="hh_uniq_positions.csv"

positions="Junior Middle Senior"

awk -F',' '$3 != "-" && $3 != "" {count[$3]++} END {
    for (pos in count) 
        print pos, count[pos]
}' "$INPUT_FILE" > temp_counts.txt

{
    echo "\"name\",\"count\""
    for pos in $positions; do
        count=$(grep -w "$pos" temp_counts.txt | awk '{print $2}')
        echo "\"$pos\",${count:-0}"
    done
} > "$OUTPUT_FILE"

rm -f temp_counts.txt