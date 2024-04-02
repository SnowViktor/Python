from random import randint

print('\nNumber Guessing Game')
low = int(input('\nLower limit: '))
high = int(input('Upper limit: '))
answer = randint(low, high)
record = 0

while True:
    user = int(input(f'\n〈{low} ~ {high}〉: '))
    record += 1

    if user == answer:
        print(f'\n[{user}] Correct')
        print(f'Guessed {record} times.')
        break
    elif user < answer:
        low = user
    elif user > answer:
        high = user