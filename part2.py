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
user_guess = input("Guess a letter: ").lower()

display = ""

for letter in choosen_word:
    if user_guess == letter:
        display += user_guess

    else:
        display += "_"

print(display)