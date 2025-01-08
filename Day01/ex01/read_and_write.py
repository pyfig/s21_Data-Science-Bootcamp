def read_and_write():
    input_file = "ds.csv"
    output_file = "ds.tsv"

    try:
        with open(input_file, 'r', encoding='utf-8') as csv_file:
            lines = csv_file.readlines()

        with open(output_file, 'w', encoding='utf-8') as tsv_file:
            for line in lines:
                fields = line.strip().split('","')
                fields[0] = fields[0].lstrip('"')
                fields[-1] = fields[-1].rstrip('"')
                tsv_file.write('\t'.join(fields) + '\n')

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_and_write()
