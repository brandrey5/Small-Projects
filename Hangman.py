# Author: Brandon Reyes-Perez
# Date Created: 10/30/2025
# Last Modified: 11/06/2025
# Reference: https://www.codedex.io/projects/build-a-word-guessing-game-with-python

import random

WORD_BANK = ['plug', 'import', 'word', 'teeth']

hangmanStages = ['''
    +---+
    |   |
        |
        |
        |
    ======
''', '''
    +---+
    |   |
    O   |
        |
        |
    ======
''', '''
    +---+
    |   |
    O   |
    |   |
        |
    ======
''', '''
    +---+
    |   |
    O   |
    |\  |
        |
    ======
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
    ======
''', '''
    +---+
    |   |
    O   |
   /|\  |
     \  |
    ======
''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
    ======
''']

word = random.choice(WORD_BANK)

guessedWord = ['_'] * len(word) # a list

attempts = 7
curr = 0 # index for which hangman stage to use

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord)) # print contents of list
    guess = input('Guess a letter: ')

    while len(guess) > 1 or not guess.isalpha(): # check if guess is a valid letter
        guess = input('Guess a singular letter: ')

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess # replace blank with correct letter
        print('Great guess!')
    else:
        attempts -= 1
        print(hangmanStages[curr])
        curr += 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word')
        break

    if attempts == 0 and '_' in guessedWord:
        print('\nYou ran out of attempts! The word was: ' + word)
