#%run codeword.py
#Aleeza Tarannum Freshman Project
import random

def play_game():
    count = 0
    guesses = []
    words = ["ARRAY", "ERROR", "CLASS", "LOOPS", "BYTES"]
    secret_word = random.choice(words)

    while count < 7:
        guess = input("Guess the programming word: ").upper()
        guesses.append(guess)

        if len(guess) != 5:
            print("Your guess must be 5 letters!")
            continue

        count += 1

        if guess == secret_word:
            print("You got it!")
            break
        else:
            print("Not quite!")

        remaining = list(secret_word)

        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                print(guess[i], "🟩", end=" ")
                remaining.remove(guess[i])
            elif guess[i] in remaining:
                print(guess[i], "🟨", end=" ")
                remaining.remove(guess[i])
            else:
                print(guess[i], "⬜", end=" ")

        print()

        if count == 7:
            print("Game over!")
            print("The word was:", secret_word)

play_game()