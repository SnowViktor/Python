import random

def Password(length: int) -> str:
    '''
    Password is ASCII characters
    '''
    password_list = list(random.sample(' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' + "'", 95))
    password = ''.join(password_list[:length])
    return password