import sys

def email_to_name(email):
    username = email.split('@')[0]
    parts = username.split('.')
    if len(parts) == 2:
        first_name, last_name = parts
        return first_name.capitalize(), last_name.capitalize()
    else:
        return username.capitalize(), ''

def names_extractor():
    if len(sys.argv) != 2:
        print("Usage: python3 names_extractor.py <path_to_file>")
        return
    
    input_file = sys.argv[1]
    output_file = "employees.tsv"

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write("Name\tSurname\tE-mail\n")
            
            for line in infile:
                email = line.strip()
                if not email:
                    continue
                first_name, last_name = email_to_name(email)
                outfile.write(f"{first_name}\t{last_name}\t{email}\n")
        
        print(f"Таблица сохранена в '{output_file}'")

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    names_extractor()
