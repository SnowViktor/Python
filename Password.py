from random import sample

def password(length: int) -> str:
    '''
    The password is ASCII charcters and the maximum length of the password is 95 charcters.
    '''
    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    str_password = ''.join(PASSWORD[:length])
    return str_password