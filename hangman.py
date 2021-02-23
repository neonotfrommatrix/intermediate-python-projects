#we need the word word.py it is almost any list of words
#so our computer will pick one of these words

import random
from words import words #this will get the word file
import string

# print(words) to get all words

#1
def get_valid_word(words):
  #will take in list and randomly choose f4rom that list
    word = random.choice(words)  # randomly chooses something from the list
    #if a black space or words, it will choose a different word
    while '-' in word or ' ' in word:
        word = random.choice(words)

  #our words will be all upperccase
    return word.upper()

#2
def hangman():
  #keeps track of the letters we use
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    #this imports words of uppercase words in english dictionary
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6
#LAST
#when length of word letters is greater than zero, iterate
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        #the join keeps  strings and they will be seperated by as space
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


#3 GETS USER INPUT uppercase so all equual
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
#if invalid, minus a life
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
#if letter is in used letters, they have already used it  and its invalid guess
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
