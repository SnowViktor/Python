from random import sample

def caesar_cipher(text: str, offset: int) -> str:
    '''
    >>> caesar_cipher('Hello, World!', 1)
    'Ifmmp, Xpsme!'
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    OFFSET_MAP = {c: ALPHABET[(i + offset) % 26] for i, c in enumerate(ALPHABET)}
    OFFSET_MAP.update({c.upper(): ALPHABET[(i + offset) % 26].upper() for i, c in enumerate(ALPHABET)})
    
    return ''.join(OFFSET_MAP.get(char, char) for char in text)

def random_generator(length: int) -> str:
    '''
    The password is ASCII characters and the maximum length of the password is 95 characters.
    '''

    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    return ''.join(PASSWORD[:length])