import pathlib
import random
from string import ascii_letters

WORD_LIST = pathlib.Path("wordlist.txt")
WORD_LIMIT = 5

words = [
    word.upper()
    for word in WORD_LIST.read_text(encoding="utf-8").split("\n")
    if (word) == WORD_LIMIT and all(letter in ascii_letters for letter in word)
]
secret_word = random.choice(words)

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()

    if guess == secret_word:
        print("Correct")
        break


    correct_letters = {
        letter for letter, correct in zip(guess, secret_word) if letter == correct
    }
    misplaced_letters = set(guess) & set(secret_word) - correct_letters
    wrong_letters = set(guess) - set(secret_word)

    print("Correct letters:", ",".join(sorted(correct_letters)))
    print("Misplaced letters:", ",".join(sorted(misplaced_letters)))
    print("Wrong letters", ",".join(sorted(wrong_letters)))

else:
    print(f"The word was {secret_word}")


def main():

    # Pre-process
    word = get_random_word(...)

    # Process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(...)
        if guess == word:
            break
    
    # Post-process
    else:
        game_over(...)