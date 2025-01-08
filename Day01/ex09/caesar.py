import sys

def caesar_cipher():
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of arguments. Usage: python3 caesar.py <encode|decode> <text> <shift>")

    action = sys.argv[1]
    text = sys.argv[2]
    
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer.")

    if any(ord(char) < 32 or ord(char) > 126 for char in text):
        raise Exception("The script does not support your language yet.")

    if action == "decode":
        shift = -shift
    elif action != "encode":
        raise Exception("Invalid action. Use 'encode' or 'decode'.")

    result = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            new_char = char
        result.append(new_char)

    print(''.join(result))


if __name__ == "__main__":
    caesar_cipher()
