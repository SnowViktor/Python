from random import sample

def caesar_cipher(text: str, manual: bool, offset: int = 1, interval: str = ' ') -> str:
    '''
    manual =
    ### True ->> offset can be changed\n
    ### False ->> interval can be changed
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    list_new_text = []

    while True:
        for charcter in text:
            if charcter.isupper():
                upper_charcter = True
                charcter = charcter.lower()
            elif not charcter.isupper():
                upper_charcter = False 
            
            if charcter in ALPHABET:
                position = ALPHABET.find(charcter)
                new_position = (position + offset) % 26
                new_charcter = ALPHABET[new_position]
                if upper_charcter:
                    new_charcter = new_charcter.upper()
                new_text += new_charcter
            elif charcter not in ALPHABET:
                new_text += charcter
        
        if not manual:
            list_new_text.append(new_text)
            new_text = ''
            offset += 1
            if offset < 26:
                pass
            elif offset >= 26:
                str_list_new_text = interval.join(list_new_text)
                return str_list_new_text
        elif manual:
            return new_text

def random_generator(length: int) -> str:
    '''
    The password is ASCII charcters and the maximum length of the password is 95 charcters.
    '''
    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    str_password = ''.join(PASSWORD[:length])
    return str_password
