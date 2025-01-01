from random import sample
from itertools import permutations

def generate_secret_number():
    return ''.join(sample("0123456789", 4))

def get_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
    return bulls, cows

def auto_guess(secret_number, stats):
    attempts = 0
    possible_guesses = [''.join(p) for p in permutations("0123456789", 4)]
    feedback = []

    while possible_guesses:
        guess = possible_guesses.pop(0)
        attempts += 1
        bulls, cows = get_bulls_and_cows(secret_number, guess)
        print(f"Attempt {attempts}: Guess = {guess}, Result = {bulls}A{cows}B")
        
        if bulls == 4:
            print(f"Auto-guessed the number {secret_number} in {attempts} attempts.")
            stats.append(attempts)
            break
        
        feedback.append((guess, bulls, cows))
        possible_guesses = [g for g in possible_guesses if all(get_bulls_and_cows(g, f[0]) == (f[1], f[2]) for f in feedback)]
        possible_guesses.sort(key=lambda x: sum(get_bulls_and_cows(x, f[0])[0] for f in feedback), reverse=True)

def main():
    stats = []
    while True:
        secret_number = generate_secret_number()
        attempts = 0
        print("\nWelcome to the 1A2B (Bulls and Cows) game!")
        print("I have generated a 4-digit secret number. Try to guess it!\n")

        while True:
            guess = input("Enter your guess (or type 'auto' for auto-guess): ")
            if guess.lower() == 'auto':
                auto_guess(secret_number, stats)
                break

            if len(guess) != 4 or not guess.isdigit():
                print("Invalid input. Please enter a 4-digit number.")
                continue

            attempts += 1
            bulls, cows = get_bulls_and_cows(secret_number, guess)
            print(f"{bulls}A{cows}B")

            if bulls == 4:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break

        play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            if stats:
                avg_attempts = sum(stats) / len(stats)
                print(f"AI's average attempts to guess the number: {avg_attempts:.2f}")
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()