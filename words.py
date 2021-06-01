import random


def load_words():
    """
    this function help to load more word by updating word_list (list)    
    Example :-
        word_list = ["learning", "kindness", "joy", "kiet", "good"] (old)
        word_list = ["learning", "kindness", "joy", "kiet", "good" ,"hello"] (new)
    """
    word_list = ["learning", "kindness", "joy", "kiet", "good", "paining"]

    # uncomment the below for testing

    WORDLIST_FILENAME = "words.txt"
    # name of the file is stored in a variable
    inFile = open(WORDLIST_FILENAME, 'r')
    # input file is opened in read only mode
    line = inFile.readline()
    # reads line by line from the file's object
    word_list = str.split(line)
   # splits the line into words...and if there were string without spaces in between it splites that into single characters
    return word_list
# returns wordlist


def choose_word():
    """
    word_list (list): list of words (strings)
    this function return one random world from list
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
