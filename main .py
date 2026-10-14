
# -----------------------------------------------------------
#                         HANGMAN GAME
# -----------------------------------------------------------
import random

words = ["confident", "brave", "honest", "improve", "achieve"]

comp = random.choice(words)

guessed_letter = []

hidden_word = ["_"] * len(comp)

attempts = 6

while attempts > 0:
    print(hidden_word)
    print("Remaining attempts",attempts)

    guess = input("Guess the letter ").lower()

    if guess in guessed_letter:
        print("you already guessed this letter")

    else:
        guessed_letter.append(guess)

        if guess in comp:
            print("correct guess!")

            for i in range(len(comp)):
                if comp [i] == guess:
                    hidden_word [i] = guess

        else:
            attempts -= 1
            print("wrong guess!")

    if "_" not in hidden_word:
        print("you won!")
        break
if attempts == 0:
    print("you lose!")
    print("the word was" , comp) 
    
    