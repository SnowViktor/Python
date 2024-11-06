from random import sample

def caesar_cipher(text: str, offset: int) -> str:
    '''
    >>> caesar_cipher('Python 3.13.0', 1)
    'Qzuipo 4.24.1'
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    DIGITS = '0123456789'

    OFFSET_MAP = {a: ALPHABET[(i + offset) % 26] for i, a in enumerate(ALPHABET)}
    OFFSET_MAP.update({a.upper(): ALPHABET[(i + offset) % 26].upper() for i, a in enumerate(ALPHABET)})
    OFFSET_MAP.update({d: DIGITS[(int(d) + offset) % 10] for d in DIGITS})
    
    return ''.join(OFFSET_MAP.get(char, char) for char in text)

def random_generator(length: int) -> str:
    '''
    The password is ASCII characters and the maximum length of the password is 95 characters.
    '''

    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    return ''.join(PASSWORD[:length])