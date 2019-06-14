alpha = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):

    for index in range(len(alpha)):
        if letter.lower() == alpha[index]:
            return index

def rotate_character(char, rot):

    if not char.isalpha():
        return char

    in_pos = alphabet_position(char)
    new_pos = (in_pos + rot) % len(alpha)
    
    if(alpha[in_pos] == char):
        return alpha[new_pos]
    else:
        return alpha[new_pos].upper()
