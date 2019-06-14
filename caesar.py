from helpers import alphabet_position, rotate_character, alpha

def encrypt(text, rot):
    c_text = ""

    for item in text:
        c_text += rotate_character(item, rot)

    return c_text

def main():
    from sys import argv, exit

    if len(argv) < 2:
        print("usage: python caesar.py n")
        exit()
    if not argv[1].isdigit():
        print("usage: python caesar.py n")
        exit()
    
    text = input("Type a message: ")
    rotate = int(argv[1])
    print(encrypt(text, rotate))

if __name__ == "__main__":
    main()