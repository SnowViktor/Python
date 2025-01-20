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

def vigenere_cipher(text: str, key: str) -> str:
    '''
    >>> vigenere_cipher('Python 3.13.1', 'key')
    'Pcrrsl 7.17.1'
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    DIGITS = '0123456789'

    def shift(char, offset):
        if char in ALPHABET:
            return ALPHABET[(ALPHABET.index(char) + offset) % 26]
        elif char in DIGITS:
            return DIGITS[(int(char) + offset) % 10]
        return char
    
    key = key.lower()
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    return ''.join(shift(char, ALPHABET.index(key[i])) for i, char in enumerate(text))

if __name__ == '__main__':
    print(caesar_cipher('Python 3.13.1', 1))
    print(vigenere_cipher('Python 3.13.1', 'key'))
