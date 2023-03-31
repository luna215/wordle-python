import pathlib
import random

WORD_LIST = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in WORD_LIST.read_text(encoding="utf-8").strip().split("\n")
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
