import random


"""
 A general quick for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the letters guessed
4. Reveal letters already guessed
5. Create the win condition
"""


word_bank = ["basketball", "shoes", "shoot", "football", "hang", "victor", "nike", "guess", "jordan", "you win"]
random_word = random.choice(word_bank)
print(random_word)

letters_guessed = []


current_guess = ""
while current_guess != "quit":
    current_guess = input("Guess a letter")
    letters_guessed.append(current_guess)

    print(letters_guessed)



