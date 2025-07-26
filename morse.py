MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += '/ '
    return cipher

def decrypt(morse_symbols):
    decipher = ''
    morse_char = ''
    inv_morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    for symbol in morse_symbols:
        if symbol == ' ':
            if morse_char in inv_morse_dict:
                decipher += inv_morse_dict[morse_char]
            morse_char = ''
        elif symbol == '/':
            if morse_char in inv_morse_dict:
                decipher += inv_morse_dict[morse_char]
            decipher += ' '
            morse_char = ''
        else:
            morse_char += symbol
    if morse_char in inv_morse_dict:
        decipher += inv_morse_dict[morse_char]
    return decipher.strip()
