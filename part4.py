import random 

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


list_of_words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'kiwi', 'lemon'
]


lives = 6

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
    

    if user_guess not in choosen_word:
        lives -= 1

    if lives == 0:
        game_over = True
        print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")


    print(stages[lives])
    print(f"You have {lives} lives left")