import random 

list_of_words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'kiwi', 'lemon'
]

choosen_word = random.choice(list_of_words)
print(choosen_word)

placeholder = ""
for letter in choosen_word:
    placeholder += "_"
print(placeholder)


game_over = False

correct_guesses = []

while not game_over:
    user_guess = input("Guess a letter: ").lower()

    display = ""

    for letter in choosen_word:
        if user_guess == letter:
            correct_guesses.append(letter)
            display += user_guess
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")