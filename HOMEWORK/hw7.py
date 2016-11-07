# ----------------------------------------------------------
# HW 7
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent in total:  2.5
# Collaborators (if any) and resources used (if any):  
# Feedback: What was the hardest part of this assignment?
#   Figuring out why g was not in "G". Because it wasn't
#   g.upper(). oh well
# Feedback: Any suggestions for improving the assignment?	
#   <your answer here>
# ----------------------------------------------------------

import random

#-----------------SECTION -1------------------
#Draws Gallows
def draw_gallows(misses):
    '''
    (int) -> None

    Print a representation of the hangperson gallows.  The parameter
    misses is the number of missed words.  7 misses means
    that the player has lost (and the full gallows gets printed).
    '''
    if (misses < 0 or misses > 7):
        raise Exception("Invalid number of missed words when attempting to print the gallows.")


    print 
    print 
    print '       |||========|||'
    if misses > 0:
        print '       |||         |'
    else:
        print '       |||          '

    if misses > 1:
        print '       |||         O'
    else:
        print '       |||          '

    if misses > 2:

        if misses > 4:
            print '       |||        /|\\'
        elif misses > 3:
            print '       |||        /| '
        else:
            print '       |||        /  '
    else:
        print '       |||           '

    if misses > 5:
        if misses > 6:
            print '       |||        / \\'
        else:
            print '       |||        /  '
    else:
        print '       |||           '

    print '       |||'
    print '       |||'
    print '     ================='
    print  


#-----------------SECTION 1------------------
#Runs all of the smaller programs
def play_game():

    misses = 0
    # our list of possible words.  add or modify the
    # list as you want    
    wordlist = ['SUNNY','BEES','GRASS','BUNNY','ABJECT','ABERRATION','ABJURE','ABROGATE','COGENT','COGNIZANT','COMMENSURATE','ENERVATE','SCIENCE','FRACTIOUS','GARRULOUS','INVETERATE','MUNIFICENT','STRASH','ONEROUS','PREDILECTION','SPURIOUS','VOCIFEROUS','TIRADE']
    guessedletters = []
    # example for getting a random word from the word list
    secretword = random.choice(wordlist)
    word = word_to_list(secretword)
    while misses<7:

        guess = get_guess(guessedletters)
        guessedletters += [guess]
        word,misses,win = process_guess(guess,word,secretword,guessedletters,misses)
        draw_gallows(misses)
        print "Guessed Letters:", display_letters(guessedletters)
        print
        print "Current Word:", display_word(word)
        print
        if win:
            print "Congratulations! You win!!!"
            print
            break

    if not win:
        print "Sorry, you lose!!!"
        print "The word was", secretword.lower().capitalize()
        print
    
#-----------------SECTION 2------------------
#Get's the guess
def get_guess(guessedletters):

    while True:
        guess = raw_input("Please enter a guess: ").upper()
        if len(guess) > 1:
            print "Invalid Input: Guess Only One Letter!"
            print
        elif len(guess)<1:
            print "Invalid Input: You Must Guess Something!"
            print
        elif not guess.isalpha():
            print "Invalid Input: Only Alphabetic Characters Allowed!"
            print
        elif guess in guessedletters:
            print "Invalid Input: You Have Already Guessed This Letter!"
            print

        else:
            print
            return guess

#-----------------SECTION 3------------------
#Adds to misses, checks if there's a win, and updates the word
def process_guess(letter,word,secretword,guessedletters,misses):

    win = False
    if letter in secretword:
        for i in range(len(word)):
            if word[i][0] == letter:
                word[i][1] = True
    else:
        misses += 1

    correctcount = 0
    for i in range(len(word)):
        if word[i][1] == True:
            correctcount += 1

    if correctcount == len(secretword):
        win = True
    
        

    return word,misses,win


#-----------------SECTION 4------------------
#Converts the word to a list

def word_to_list(word):
    lst = []
    for char in word:
        temp = []
        temp += [char]
        temp += [False]
        lst += [temp]

    return lst



#-----------------SECTION 5------------------
#Display Word and Guessed Letters to Users
def display_word(word):

    textdisplay = ""
    for sublist in word:
        if sublist[1] == True:
            textdisplay += sublist[0]+" "
        else:
            textdisplay += "_ "

    return textdisplay

def display_letters(guessedletters):

    letterdisplay = ""
    for char in guessedletters:
        letterdisplay += char+" "
    return letterdisplay


#-----------------SECTION 6------------------
#Continues to play
def main():

    answer = "y"
    while answer.lower() in "yes":
        play_game()
        answer = raw_input("Would you like to play again? ")
        print

    print "Okay byeee!"
    



main()
