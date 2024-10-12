from random import randint

def number_guessing_game():
    low = int(input('\nLower Limit: '))
    high = int(input('Upper Limit: '))

    if low >= high:
        low, high = high, low

    answer = randint(low, high)
    record = 0

    while True:
        user = int(input(f'\n{low} ~ {high}: '))

        record += 1

        if user == answer:
            print('\nCORRECT!')
            print(f'You guessed {record} times.')
            break
        elif user < answer:
            low = user
        else:
            high = user

    play_again = input("\nContinue to the next round?(y/n): ")
    if play_again.lower() == 'y':
        number_guessing_game()

if __name__ == '__main__':
    number_guessing_game()