#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

# Navigate to the specified directory
DAY_DIR="day$1"
if [ ! -d "$DAY_DIR" ]; then
    echo "Directory $DAY_DIR does not exist."
    exit 1
fi

cd "$DAY_DIR"

# Check for any Python files and run them
for py_file in *.py; do
    if [ -f "$py_file" ]; then
        input_file="${py_file%.py}.in"
        output_file="${py_file%.py}.out"
        if [ -f "$input_file" ]; then
            python3 "$py_file" < "$input_file" > "$output_file"
            echo "Executed $py_file with input from $input_file and output to $output_file"
        else
            echo "Input file $input_file not found for $py_file"
        fi
    fi
done