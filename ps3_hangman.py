# Hangman game
#

# -----------------------------------
import random

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
    
    a = 0;
    for words in lettersGuessed:        
        if words in secretWord:
            a = a + 1
    if (len(secretWord) == a):
        return True
    else:
        return False
    
           



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    guessed = []
    outString ='';
    for a in range(0, len(secretWord)):
        guessed = guessed + ['_ ']
    
    for word in lettersGuessed:
        for a in range(0, len(secretWord)):
            if (word == secretWord[a]):
                guessed[a] = word;
                
    for a in range (0, len(secretWord)):
        outString = outString + guessed[a]
    
    return outString
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabetList = []
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z '
    
    alphabetList = alphabet.split();
    
    for word in lettersGuessed:
        if word in alphabetList:
            alphabetList.remove(word)
    
    return(''.join(alphabetList))
                
    

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
    guessNumber = 8
    userGuesses = []
    previousInput = []
    
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is '+ str(len(secretWord)) +' letters long.')
    print ('-------------')
    while (guessNumber > 0):
        print ('You have ' + str(guessNumber) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(userGuesses))
        userInput = input('Please guess a letter: ')  
       
        userGuesses.append(userInput)        
        if userInput in previousInput:
            print ('Oops! You\'ve already guessed that letter:' + getGuessedWord(secretWord, userGuesses) )
        elif userInput in secretWord:
            print('Good guess: ' + getGuessedWord(secretWord, userGuesses))
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, userGuesses))
            guessNumber = guessNumber - 1;
        previousInput.append(userInput)
        print ('------------')
        if '_ ' not in getGuessedWord(secretWord, userGuesses):
            print ('Congratulations, you won!')
            break;
        if (guessNumber == 0):
            print ('Sorry, you ran out of guesses. The word was ' + secretWord)
        
        
    
    






# Runs the program
 

secretWord = chooseWord(wordlist).lower()
secretWord = 'tact'
hangman(secretWord)