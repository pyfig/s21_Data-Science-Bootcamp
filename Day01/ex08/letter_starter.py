import sys

def find_name_and_generate_letter(email, file_path='employees.tsv'):
    try:
        with open(file_path, 'r') as f:
            rows = f.readlines()
        
        for row in rows[1:]:
            name, surname, email_in_file = row.strip().split('\t')
            if email_in_file == email:
                print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                return
        
        print("Почта не найдена.")
    except Exception as e:
        print(f"{e}")

def letter_starter():
    if len(sys.argv) != 2:
        print("Usage: python3 letter_starter.py <email>")
    else:
        find_name_and_generate_letter(sys.argv[1])    

if __name__ == "__main__":
    letter_starter()