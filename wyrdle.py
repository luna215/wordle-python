
for guess_num in range(1, 7):
    guess = input("Guess a word").upper()

    if guess == "SNAKE":
        print("Correct")

    else:
        print("Wrong")