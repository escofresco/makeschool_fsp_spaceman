import os
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word_set: set, letters_guessed: set):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # return if the original set is the intersection of the two sets
    return secret_word_set == secret_word_set & letters_guessed

def get_guessed_word(secret_word: str, letters_guessed: set):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    return ''.join([letter if letter in letters_guessed
                    else '_' for letter in secret_word])


def is_guess_in_word(guess: str, secret_word_set: set):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    return guess in secret_word_set


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    secret_word_set = set(secret_word)
    letters_guessed = set()

    guess_count = 7
    while guess_count > 0:
        clear()
        print('Enter letters to guess a word.\n'
              f'You have {guess_count} guesses remaining')
        print(get_guessed_word(secret_word, letters_guessed))
        letter = input('Guess: ')
        letters_guessed.add(letter)
        if letter not in secret_word_set:
            guess_count -= 1
        if is_word_guessed(secret_word_set, letters_guessed):
            print('You win')
            break
    else:
        print('You lose')

def clear():
    # thanks @poke
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls' if os.name == 'nt' else 'clear')



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
