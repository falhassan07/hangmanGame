import random 

list_of_words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'kiwi', 'lemon'
]

choosen_word = random.choice(list_of_words)
print(choosen_word)

user_guess = input("Guess a letter: ").lower()

for letter in choosen_word:
    if user_guess == letter:
        print("Right")

    else:
        print("Wrong")