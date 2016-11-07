#COSC 101
#Lab 07

import random
import time

def dragon_game():
    #*** DO NOT MODIFY THIS FUNCTION ***
    while (True): #loops until the user doesn't want to play anymore
        if (single_game()):#plays a single game and checks to see if you won
            print "You retrieved all of your homework!  You win!!"
        else:
            print "Uh-oh, you became dinner.  Game Over!"
        again = raw_input("Play again?  Enter 'y' for yes or anything else to quit: ")
        if (again.lower() != "y"):#stops looping if the user doesn't want to play
            break
    print "Thanks for playing!"



#************* All of your code for Lab 07 will go below *************

def single_game():
    '''(None) -> (bool)
    Begins a game and
    continues to prompt new locations
    so long as you haven't collected 3
    homework or been eaten
    '''
    visited = [] #stores the locations you have already visited
    egg_loc = random.randint(1,4) #randomly selects a location as the "egg location"
    homework_collected = 0
    display_intro()
    while homework_collected!=3:
        chosen_loc = get_location(visited)
        visited += [chosen_loc]
        if check_location(chosen_loc,egg_loc):
            return False
        else:
            homework_collected+=1
        
            
    return True


def display_intro():
    '''(None) -> (None)
    Displays meaningful introductory
    test to inform the user of their
    unfortunate predicament
    '''
    print "-----------------------------------------------"
    print "Welcome to the interactive Dragon Game (C)1987"
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
    time.sleep(0.25)
    print "Test your luck to see if you can retrieve all"
    time.sleep(0.25)
    print "of the homework you foolishly left scattered"
    time.sleep(0.25)
    print "around Colgate University"
    time.sleep(0.5)
    print "or..."
    time.sleep(0.5)
    print "If you will meet your bitter end in the jaws"
    time.sleep(0.25)
    print "of a terrifying dragon!"
    time.sleep(0.25)
    print "-----------------------------------------------"
    print
    variable = raw_input("Press enter to begin your adventure!")
    

def get_location(visited):
    '''(list) -> (int)
    takes a list of locations, visted
    and returns the next location to visit, int
    '''
    #prompts the user to enter a location number
    #should keep prompting the user until they
    #enter a valid input
    while True:
        print
        print "Which location will you visit next?"
        print "1 - Olin Hall"
        time.sleep(0.25)
        print "2 - West Hall"
        time.sleep(0.25)
        print "3 - McGregory Hall"
        time.sleep(0.25)
        print "4 - Underground Tunnel"
        time.sleep(0.25)
        chosen_loc = raw_input("Location: ")
        if not chosen_loc.isdigit():
            time.sleep(0.5)
            print "Invalid Number! Try again."
            print
        elif int(chosen_loc) in visited:
            time.sleep(0.5)
            print "You've already been there! Try again."
            print
        elif int(chosen_loc)>4 or int(chosen_loc)<1:
            time.sleep(0.5)
            print "Invalid Number! Try again."
            print
        

        else:
            return int(chosen_loc)
            
            


def check_location(chosen_loc, egg_loc):
    '''(int,int) -> (bool)
    Checks if the two locations int and int
    are the same and returns whether or not
    you were eaten
    '''
    #FINISH THIS FUNCTION!
    #Returns True if the user is successful
    #Returns False if user gets eaten

    dragon = False
    eat = False
    hunger = random.randint(0,1)
    if chosen_loc == egg_loc:
        dragon = True
        if hunger == 1:
            eat = True
    print
    print "You approach the location..."
    time.sleep(1)
    print "The air around you feels damp..."
    time.sleep(1)
    print "You turn on your flashlight and look around..."
    time.sleep(1)

    #Gets eaten
    if dragon and eat:
        print "You see a fearsome dragon!"
        time.sleep(1)
        print "She opens her mouth wide and..."
        time.sleep(2)
        print "attacks! Swallowing everything except your right shoe"
        time.sleep(1)
        print "which falls to the floor as a warning for future"
        time.sleep(1)
        print "trespassers."
        time.sleep(1)
        print
        return True

    #Encounters dragon but escapes
    elif dragon and not eat:
        print "You see a fearsome dragon!"
        time.sleep(1)
        print "She opens her mouth wide and..."
        time.sleep(2)
        print "lets out a giant snore! Phew, she's asleep"
        time.sleep(1)
        print "despite your screams."
        time.sleep(1)
        print "You grab your homework and get out!"
        time.sleep(1)
        print
        return False

    else:
        print "You see a brief white flash in the corner"
        time.sleep(1)
        print "It's your homework..."
        time.sleep(1)
        print "You grab your homework and get out!"
        time.sleep(1)
        print
        return False
        
        
    
