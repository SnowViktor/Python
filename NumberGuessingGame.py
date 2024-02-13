import random

print('\nNumber Guessing Game')
low = int(input('\nLower limit: '))
high = int(input('Upper limit: '))
answer = random.randint(low, high)
record = 0

while True:
    user = int(input('\n〈' + str(low) + ' ~ ' + str(high) + '〉: '))
    record += 1
    if user == answer:
        print(f'[{user}] Correct')
        print(f'\nGuessed {record} times.')
        break
    elif user < answer:
        print(f'[{user}] Wrong')
        low = user
    elif user > answer:
        print(f'[{user}] Wrong')
        high = user