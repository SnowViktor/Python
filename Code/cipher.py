def caesar_cipher(text: str, offset: int) -> str:
    '''
    >>> caesar_cipher('Python 3.13.1', 1)
    'Qzuipo 4.24.2'
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    DIGITS = '0123456789'

    OFFSET_MAP = {a: ALPHABET[(i + offset) % 26] for i, a in enumerate(ALPHABET)}
    OFFSET_MAP.update({a.upper(): ALPHABET[(i + offset) % 26].upper() for i, a in enumerate(ALPHABET)})
    OFFSET_MAP.update({d: DIGITS[(int(d) + offset) % 10] for d in DIGITS})
    
    return ''.join(OFFSET_MAP.get(char, char) for char in text)