# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # converts secretword to a list so that set can be used
    # checks if secretword is a subset or equal to lettersguessed
    # returns True if all letters of secretWord are found in lettersGuessed
    return set(list(secretWord)) <= set(lettersGuessed)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed = '' # initalize string for presentation

    for letter in secretWord:
      if letter in lettersGuessed: # where the letter is in both lists, it gets added to guessed
        guessed += letter
      else:
        guessed += '_' # if the letter isn't found an underscore is used
    guessed = " ".join(guessed) # maintains spacing between characters
    return guessed

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase) # generates a lowercase string of a to z, converted to a list.
    avail_letters = [x for x in alphabet if x not in lettersGuessed] # list comprehension syntax to remove letters already guessed
    return "".join(avail_letters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_num = 8
    guesses = ''

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-------------")

    
    
    while isWordGuessed(secretWord, guesses) == False:
      print("You have", guesses_num, "guess(es) left.")
      print("Available letters:", getAvailableLetters(guesses))
      guess = input("Please guess a letter: ").lower()

      if guesses_num < 2:
        print("Sorry, you ran out of guesses. The word was '", secretWord,"'.")
        break
      elif guess in secretWord and guess in guesses:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guesses))
        print("-------------")
      elif guess in secretWord:
        guesses += guess
        guesses_num -= 1
        print("Good guess:", getGuessedWord(secretWord, guesses))
        print("-------------")
      elif guess not in secretWord:
        guesses_num -= 1
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, guesses))
        guesses += guess
        print("-------------")
    else:
      print("Congratulations, you won!")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
