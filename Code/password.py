from random import sample

def caesar_cipher(text: str, offset: int) -> str:
    '''
    >>> caesar_cipher('Hello, World!', 1)
    'ifmmp, xpsme!'
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    offset_text = ''

    for character in text:
        if character.lower() in ALPHABET:
            character_position = ALPHABET.find(character.lower())
            offset_character = ALPHABET[(character_position + offset) % 26]
            if character not in ALPHABET:
                offset_character.upper()
            offset_text += offset_character
        elif character not in ALPHABET:
            offset_text += character
    
    return offset_text

def random_generator(length: int) -> str:
    '''
    The password is ASCII characters and the maximum length of the password is 95 characters.
    '''

    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    return ''.join(PASSWORD[:length])