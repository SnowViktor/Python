from random import sample

def random_generator(length: int) -> str:
    '''
    The password is ASCII characters and the maximum length of the password is 95 characters.
    '''

    PASSWORD = sample(' !\'"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', 95)
    return ''.join(PASSWORD[:length])
