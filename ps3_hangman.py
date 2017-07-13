# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
secretWord = 'apple'

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    counter=0
    for letter in secretWord:
        for intLG in range(0, len(lettersGuessed)):
            if letter == lettersGuessed[intLG]:
                counter +=1
            #print letter
            #print counter
            #print letterGuessed[intLG]
    if counter >= len(secretWord):
       # print 'Word found!'
        return True
    else: 
       # print 'Broken program'
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    counter = 0
    guess = ''
    for letter in secretWord:
        for intLG in range(0, len(lettersGuessed)):
            if letter == lettersGuessed[intLG]:
                counter +=1
                guess = guess + letter
                break
        else: 
            guess = guess + '_'
    #print guess
    return guess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters= ""
    intLG = 0
    
    for letter in string.ascii_lowercase:
        for intLG in range(0, len(lettersGuessed)):
            if letter != lettersGuessed[intLG]:
                availableLetters = availableLetters + letter
            elif letter == lettersGuessed[intLG]: 
                break
    FVLetters = ''
    for intalet in range(0, 26):#for letters in the alphabet
        if availableLetters.count(string.ascii_lowercase[intalet]) >= len(lettersGuessed):
            #print availableLetters.count(string.ascii_lowercase[intalet]),
            FVLetters += string.ascii_lowercase[intalet] 
        #print aletters.count
    return FVLetters            

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
    # FILL IN YOUR CODE HERE...
    guesscnt = 8
    lettersGuessed = []
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    # JUNK: for character in secretWord:
    # JUNK Cont:   print '_ ',
    print '-------------',
    while isWordGuessed(secretWord, lettersGuessed) != True and  guesscnt >0:
            
            print '\nYou have ' + str(guesscnt) +  ' guesses left'
            print 'Available letters: ' + getAvailableLetters(lettersGuessed),
            user_inp = raw_input("Please guess a letter:")
            user_inp2 = user_inp.lower()
            if user_inp2 in lettersGuessed:
                    print"Opps! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
                    pass
            elif user_inp2 in secretWord:
                lettersGuessed.append(user_inp2)
                print'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
            elif user_inp2 not in secretWord:
                lettersGuessed.append(user_inp2)
                print"Opps! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
                guesscnt -=1
            else:
                #print 'game done'
                return 'Congratulations, you won!'
    print '-------------',
    if guesscnt <=0:
        return 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
    elif isWordGuessed(secretWord, lettersGuessed) == True:
        return 'Congratulations, you won!'
    #print 'Please guess a letter: '
    #available/letters/guess words needs a character restriction
    
    
hangman('c')





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)