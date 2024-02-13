def caesar_cipher(text: str, encrypt_or_decrypt: str, automatic_or_manual: str, offset: int = 1, interval: str = ',') -> str:
    '''
    \nencrypt_or_decrypt = 'e' or 'd'
    \nautomatic_or_manual = 'a' or 'm'
    ① 'a' change interval\n
    ② 'm' change offset
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    list_new_text = []

    while True:
        for charcter in text:
            if charcter.isupper() == True:
                upper_charcter = True
                charcter = charcter.lower()
            elif charcter.isupper() == False:
                upper_charcter = False 
            
            if charcter in alphabet:
                position = alphabet.find(charcter)
                if encrypt_or_decrypt =='e':
                    new_position = (position + offset) % 26
                elif encrypt_or_decrypt == 'd':
                    new_position = (position - offset) % 26
                new_charcter = alphabet[new_position]
                if upper_charcter == True:
                    new_charcter = new_charcter.upper()
                new_text += new_charcter
            elif charcter not in alphabet:
                new_text += charcter
        
        if automatic_or_manual == 'a':
            list_new_text.append(new_text)
            new_text = ''
            offset += 1
            if offset < 26:
                continue
            elif offset >= 26:
                str_list_new_text = interval.join(list_new_text)
                return str_list_new_text
        elif automatic_or_manual == 'm':
            return new_text