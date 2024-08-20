import random 
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(f"{placeholder}\n")
    


game_over = False

correct_guesses = []

while not game_over:

    print(f"**************************** {lives} LIVES LEFT****************************")

    user_guess = input("Guess a letter: ").lower()

    display = ""


    if user_guess in correct_guesses:
        print(f"You've already guessed {user_guess}")
    

    for letter in chosen_word:
        if user_guess == letter:
            correct_guesses.append(letter)
            display += user_guess
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
            

    print(display)


    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. \n You lose a life.")
        lives -= 1

    if lives == 0:
        game_over = True
        print(f"It was {chosen_word}\n***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])