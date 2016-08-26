
def alphabet_position(letter):


        letter = letter.lower()

        return ord(letter) - 97




def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if char.isalpha() == False:
        return char
    elif char in alphabet:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return alphabet[rotated_index]
        else:
            return alphabet[rotated_index % 26]
    elif char in alphabet2:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return alphabet2[rotated_index]
        else:
            return alphabet2[rotated_index % 26]

def encrypted(string, rot):

    rot = int(rot)

    encrypted = ''
    for char in string:
        encrypted = encrypted + rotate_character(char, rot)


    return encrypted
