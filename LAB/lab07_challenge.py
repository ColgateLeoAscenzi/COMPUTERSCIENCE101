#COSC 101
#Leo Ascenzi
#Lab 07 Challenge Edition!

import random
import time
import os


def dragon_game():
    '''Uses the difficulty and boolean
    to determine if you won and on what
    difficulty level, then prints the win
    and loss message and records the
    game data
    '''
    while (True): #loops until the user doesn't want to play anymore
        log = open("DragonGameLog.txt","a")
        win,diff = single_game()
        if win:#plays a single game and checks to see if you won
            print "You retrieved all of your homework!  You win!!"
            log.write("Yay, you retrieved all of your homework!\n")
            log.write("Let it be known that you won on %s at %s\n" % ((time.strftime("%m/%d/%Y")),(time.strftime("%H:%M:%S"))))
            log.write("The difficulty setting was: %s\n" % diff)
            log.write("------------------------------------------------\n")
            log.close()
            
        else:
            print "Uh-oh, you became dinner.  Game Over!"
            log.write("Uh-oh, you died.\n")
            log.write("Let it be known that you lost on %s at %s\n" % ((time.strftime("%m/%d/%Y")),(time.strftime("%H:%M:%S"))))
            log.write("The difficulty setting was: %s\n" % diff)
            log.write("------------------------------------------------\n")
            log.close()
        again = raw_input("Would you like to play again? ")
        if  again.lower() not in "yes":#keeps looping if user enters, y, yes, YES, Y, Yes
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
    #Selects a name for the dragon
    dragon_names = ["Ryoko","Tatsu","Vritra","Cordelia","Norberta","Tintaglia","Kalta"]
    name_selection = random.randint(0,6)
    name = dragon_names[name_selection]

    #Selects a direction for the dragon
    cardinal = ["North","South","East","West"]
    direction_selection = random.randint(0,3) #I love the rhyme
    location = cardinal[direction_selection]

    #Selects a type of homework
    types = ["math","calculus","calc III","calc II", "calc I","computer science","comp sci","comp sci 101","physics","physics 131","history","FSEM","german","german 351","chemisty","chem","psychology","psych","economics","econ"]
    actual = random.randint(0,19)
    subject = types[actual]

    #Selects dragons title
    titles = ["magestic","mythical","magical","fabled","cruel","evil","powerful","shiny","clever","quick","red","blue","green","invisible","old"]
    selected = random.randint(0,14)
    title = titles[selected]
    
    #stores the locations you have already visited
    visited = []

    #sets up firstplay counter
    firstplay = 0

    #randomly selects a location as the "egg location"
    egg_loc = random.randint(1,4)

    #Initializes homework collected
    homework_collected = 0
    display_intro()

    #Sets difficulty
    difficulty = int(raw_input("Please enter a difficulty: "))
    while difficulty<1:
        difficulty = int(raw_input("Oh come on, enter a number one or bigger you wimp: "))

    difficulty+=1
    
    #Returns true if you collect 3 homework, and false if you're eaten
    while homework_collected!=3:
        #Selects a type of homework
        types = ["math","calculus","calc III","calc II", "calc I","computer science","comp sci","comp sci 101","physics","physics 131","history","FSEM","german","german 351","chemisty","chem","psychology","psych","economics","econ"]
        actual = random.randint(0,19)
        subject = types[actual]

        #Collects the chosen location
        chosen_loc = get_location(visited,firstplay)
        firstplay += 1
        visited += [chosen_loc]

        
        if check_location(chosen_loc,egg_loc,name,location,subject,title,difficulty):
             return (False, difficulty)
        else:
            homework_collected+=1
    return (True, difficulty)


def display_intro():
    '''(None) -> (None)
    Displays meaningful introductory
    test to inform the user of their
    unfortunate predicament
    '''
    log = open("DragonGameLog.txt","a")
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
    log.write("You began your journey on a cold winter morning...\n")
    
    

def get_location(visited,firstplay):
    '''(list,int) -> (int)
    takes a list of locations, visted
    and an integer, firstplay
    and returns the next location to visit, int
    '''
    log = open("DragonGameLog.txt","a")

    #stores the names of the location
    areas = ["Olin Hall","West Hall","McGregory Hall","the Underground Tunnel"]
    
    #prompts the user to enter a location number
    #should keep prompting the user until they
    #enter a valid input
    while True:
        print
        if firstplay == 0:
            print "Which location will you visit to begin your adventure?"
        else:
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
            if firstplay == 0:
                log.write("First, you visited %s...\n" % areas[int(chosen_loc)-1])
            else:
                log.write("Then, you visited %s...\n" % areas[int(chosen_loc)-1])
            return int(chosen_loc)
            
            


def check_location(chosen_loc, egg_loc,name,location,subject,title,difficulty):
    '''(int,int,str,str,str,str,int) -> (bool)
    Checks if the two locations int and int
    are the same and returns whether or not
    you were eaten
    Also uses 3 strings name, location, subject
    and title to randomize adventure
    '''
    log = open("DragonGameLog.txt","a")
    #Returns True if the user is successful
    #Returns False if user gets eaten

    
    dragon = False
    eat = True
    dragonsnum = random.randint(1,difficulty)
    if chosen_loc == egg_loc:
        dragon = True

    print
    print "You approach the location..."
    time.sleep(1)
    print "The air around you feels damp..."
    time.sleep(1)
    print "You turn on your flashlight and look around..."
    time.sleep(1)

    #Gets eaten
    if dragon:
        print "You see a brief white flash in the corner"
        time.sleep(1)
        print "It's %s! The %s dragon of the %s" % (name,title,location)
        time.sleep(1)
        print "She opens her mouth wide and..."
        time.sleep(2)
        print "Challenges you to a guessing game?"
        time.sleep(1)
        accept = raw_input("Do you accept? ")
        if accept.lower() in "yes":
            print "The dragon asks you to guess a number between 1 and %s" % difficulty
            time.sleep(1)
            yournum = int(raw_input("Enter your guess: "))
            if yournum == dragonsnum:
                print "The dragon laughs and smiles at you with hunger in her eyes"
                time.sleep(1)
                print "She says: You're right! Being an honest dragon, I will let you be for now!"
                time.sleep(1)
                print "You grab your %s homework from the corner behind her and get out!" % subject
                time.sleep(1)
                print
                log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
                log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
                log.write("Then you won the guessing game by picking %s, which was the dragons number\n" % yournum)
                log.write("You picked it up your %s homework and left quickly\n" % subject)
                log.close()
                return False
            else:
                print "The dragon laughs and smiles at you with hunger in her eyes"
                time.sleep(1)
                print "She says: You're wrong! I will now eat you!"
                time.sleep(1)
                print "Then in one big bite, swallows you whole"
                time.sleep(1)
                print "All that's left is your right shoe,"
                time.sleep(1)
                print "which falls to the floor as a warning for future"
                time.sleep(1)
                print "trespassers."
                time.sleep(1)
                print
                log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
                log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
                log.write("Then you lost the guessing game by picking %s when the dragons number was %s\n" % (yournum,dragonsnum))
                log.write("Which resulted in you tragically meeting your demise by being eaten\n")
                log.write("Your right shoe fell off as a warning for future trespassers\n")
                log.close()
                return True
        else:
            print "The dragon is appalled by your refusal"
            time.sleep(1)
            print "She screams in rage and in her wild anger"
            time.sleep(1)
            print "Accidentally breaths fire and burns you to death"
            time.sleep(1)
            print
            log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
            log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
            log.write("Then you foolishly refused the guessing game which made the dragon enraged\n")
            log.write("Which resulted in her breathing fire and burning you to death\n")
            log.write("There was only a pile of ash left where you once stood\n")
            log.close()
            return True
    else:
        print "You see a brief white flash in the corner"
        time.sleep(1)
        print "It's your %s homework..." % subject
        time.sleep(1)
        print "You grab your homework and get out!"
        time.sleep(1)
        print
        log.write("Where you saw your %s homework lying in the corner...\n" % subject)
        log.write("You picked it up and left quickly\n")
        log.close()
        return False



    
##########################################################DEV ONLY#####################################################################
##def dragon_gamed():
##    while (True): #loops until the user doesn't want to play anymore\
##        log = open("DragonGameLog.txt","a")
##        win,diff = single_gamed()
##        if win:#plays a single game and checks to see if you won
##            print "You retrieved all of your homework!  You win!!"
##            log.write("You retrieved all of your homework!\n")
##            log.write("Let it be known that you won on %s at %s\n" % ((time.strftime("%m/%d/%Y")),(time.strftime("%H:%M:%S"))))
##            log.write("The difficulty setting was: %s\n" % diff)
##            log.write("------------------------------------------------\n")
##            log.close()
##            
##        else:
##            print "Uh-oh, you became dinner.  Game Over!"
##            log.write("Uh-oh, you became dinner.\n")
##            log.write("Let it be known that you lost on %s at %s\n" % ((time.strftime("%m/%d/%Y")),(time.strftime("%H:%M:%S"))))
##            log.write("The difficulty setting was: %s\n" % diff)
##            log.write("------------------------------------------------\n")
##            log.close()
##        again = raw_input("Play again?  Enter 'y' for yes or anything else to quit: ")
##        if again.lower() not in "yes":#stops looping if the user doesn't want to play
##            break
##    print "Thanks for playing!"
##
##
##
###************* All of your code for Lab 07 will go below *************
##
##def single_gamed():
##    #Selects a name for the dragon
##    dragon_names = ["Ryoko","Tatsu","Vritra","Cordelia","Norberta","Tintaglia","Kalta"]
##    name_selection = random.randint(0,6)
##    name = dragon_names[name_selection]
##
##    #Selects a direction for the dragon
##    cardinal = ["North","South","East","West"]
##    direction_selection = random.randint(0,3) #I love the rhyme
##    location = cardinal[direction_selection]
##
##    #Selects a type of homework
##    types = ["math","calculus","calc III","calc II", "calc I","computer science","comp sci","comp sci 101","physics","physics 131","history","FSEM","german","german 351","chemisty","chem","psychology","psych","economics","econ"]
##    actual = random.randint(0,19)
##    subject = types[actual]
##
##    #Selects dragons title
##    titles = ["magestic","mythical","magical","fabled","cruel","evil","powerful","shiny","clever","quick","red","blue","green","invisible","old"]
##    selected = random.randint(0,14)
##    title = titles[selected]
##    
##    #stores the locations you have already visited
##    visited = []
##
##    #sets up firstplay counter
##    firstplay = 0
##
##    #Sets difficulty
##    difficulty = int(raw_input("Please enter a difficulty: "))
##    while difficulty<1:
##        difficulty = int(raw_input("Oh come on, a number one or bigger... wimp...."))
##
##    difficulty+=1
##    
##    #randomly selects a location as the "egg location"
##    egg_loc = random.randint(1,4)
##
##    #Initializes homework collected
##    homework_collected = 0
##    display_introd()
##
##    #Returns true if you collect 3 homework, and false if you're eaten
##    while homework_collected!=3:
##        #Selects a type of homework
##        types = ["math","calculus","calc III","calc II", "calc I","computer science","comp sci","comp sci 101","physics","physics 131","history","FSEM","german","german 351","chemisty","chem","psychology","psych","economics","econ"]
##        actual = random.randint(0,19)
##        subject = types[actual]
##
##        #Collects the chosen location
##        chosen_loc = get_locationd(visited,firstplay)
##        firstplay += 1
##        visited += [chosen_loc]
##
##        
##        if check_locationd(chosen_loc,egg_loc,name,location,subject,title,difficulty):
##             return (False,difficulty)
##        else:
##            homework_collected+=1
##    return (True,difficulty)
##
##
##def display_introd():
##    log = open("DragonGameLog.txt","a")
##    print "-----------------------------------------------"
##    print "Welcome to the interactive Dragon Game (C)1987"
##    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
####    time.sleep(0.25)
##    print "Test your luck to see if you can retrieve all"
####    time.sleep(0.25)
##    print "of the homework you foolishly left scattered"
####    time.sleep(0.25)
##    print "around Colgate University"
####    time.sleep(0.5)
##    print "or..."
####    time.sleep(0.5)
##    print "If you will meet your bitter end in the jaws"
####    time.sleep(0.25)
##    print "of a terrifying dragon!"
####    time.sleep(0.25)
##    print "-----------------------------------------------"
##    print
##    variable = raw_input("Press enter to begin your adventure!")
##    log.write("You began your journey on a cold winter morning...\n")
##    
##    
##
##def get_locationd(visited,firstplay):
##    log = open("DragonGameLog.txt","a")
##
##    #stores the names of the location
##    areas = ["Olin Hall","West Hall","McGregory Hall","the Underground Tunnel"]
##    
##    #prompts the user to enter a location number
##    #should keep prompting the user until they
##    #enter a valid input
##    while True:
##        print
##        if firstplay == 0:
##            print "Which location will you visit to begin your adventure?"
##        else:
##            print "Which location will you visit next?"
##        print "1 - Olin Hall"
####        time.sleep(0.25)
##        print "2 - West Hall"
####        time.sleep(0.25)
##        print "3 - McGregory Hall"
####        time.sleep(0.25)
##        print "4 - Underground Tunnel"
####        time.sleep(0.25)
##        chosen_loc = raw_input("Location: ")
##        if not chosen_loc.isdigit():
####            time.sleep(0.5)
##            print "Invalid Number! Try again."
##            print
##        elif int(chosen_loc) in visited:
####            time.sleep(0.5)
##            print "You've already been there! Try again."
##            print
##        elif int(chosen_loc)>4 or int(chosen_loc)<1:
####            time.sleep(0.5)
##            print "Invalid Number! Try again."
##            print
##        
##
##        else:
##            if firstplay == 0:
##                log.write("First, you visited %s...\n" % areas[int(chosen_loc)-1])
##            else:
##                log.write("Then, you visited %s...\n" % areas[int(chosen_loc)-1])
##            return int(chosen_loc)
##            
##            
##
##
##def check_locationd(chosen_loc, egg_loc,name,location,subject,title,difficulty):
##    '''(int,int,str,str,str,str,int) -> (bool)
##    Checks if the two locations int and int
##    are the same and returns whether or not
##    you were eaten
##    Also uses 3 strings name, location, subject
##    and title to randomize adventure
##    '''
##    log = open("DragonGameLog.txt","a")
##    #Returns True if the user is successful
##    #Returns False if user gets eaten
##
##    
##    dragon = False
##    eat = True
##    dragonsnum = random.randint(1,difficulty)
##    if chosen_loc == egg_loc:
##        dragon = True
##
##    print
##    print "You approach the location..."
####    time.sleep(1)
##    print "The air around you feels damp..."
####    time.sleep(1)
##    print "You turn on your flashlight and look around..."
####    time.sleep(1)
##
##    #Gets eaten
##    if dragon:
##        print "You see a brief white flash in the corner"
####        time.sleep(1)
##        print "It's %s! The %s dragon of the %s" % (name,title,location)
####        time.sleep(1)
##        print "She opens her mouth wide and..."
####        time.sleep(2)
##        print "Challenges you to a guessing game?"
####        time.sleep(1)
##        accept = raw_input("Do you accept? ")
##        if accept.lower() in "yes":
##            print "The dragon asks you to guess a number between 1 and %s" % difficulty
##            time.sleep(1)
##            yournum = int(raw_input("Enter your guess: "))
##            if yournum == dragonsnum:
##                print "The dragon laughs and smiles at you with hunger in her eyes"
####                time.sleep(1)
##                print "She says: You're right! Being an honest dragon, I will let you be for now!"
####                time.sleep(1)
##                print "You grab your %s homework from the corner behind her and get out!" % subject
####                time.sleep(1)
##                print
##                log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
##                log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
##                log.write("And won the guessing game by picking %s, the dragons number\n" % yournum)
##                log.write("Then you picked it up your %s homework and left quickly\n" % subject)
##                log.close()
##                return False
##            
##            else:
##                print "The dragon laughs and smiles at you with hunger in her eyes"
####                time.sleep(1)
##                print "She says: You're wrong! I will now eat you!"
####                time.sleep(1)
##                print "Then in one big bite, swallows you whole"
####                time.sleep(1)
##                print "All that's left is your right shoe,"
####                time.sleep(1)
##                print "which falls to the floor as a warning for future"
####                time.sleep(1)
##                print "trespassers."
####                time.sleep(1)
##                print
##                log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
##                log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
##                log.write("And lost the guessing game by picking %s when the dragons number was %s\n" % (yournum,dragonsnum))
##                log.write("Which resulted in you tragically meeting your demise by being eaten\n")
##                log.write("Your right shoe fell off as a warning for future trespassers\n")
##                log.close()
##                return True
##            
##        else:
##            print "The dragon is appalled by your refusal"
####            time.sleep(1)
##            print "She screams in rage and in her wild anger"
####            time.sleep(1)
##            print "Accidentally breaths fire and burns you to death"
####            time.sleep(1)
##            print
##            log.write("Where you encountered %s, the %s dragon of the %s...\n" % (name,title,location))
##            log.write("Who challenged you to a random number guessing game from 1 to %s\n" % difficulty)
##            log.write("And refused the guessing game which made the dragon enraged\n")
##            log.write("Which resulted in her breathing fire and burning you to death\n")
##            log.write("There was only a pile of ash left where you once stood\n")
##            log.close()
##            return True
##            return True
##
##
##    else:
##        print "You see a brief white flash in the corner"
####        time.sleep(1)
##        print "It's your %s homework..." % subject
####        time.sleep(1)
##        print "You grab your homework and get out!"
####        time.sleep(1)
##        print
##        log.write("Where you saw your %s homework lying in the corner...\n" % subject)
##        log.write("Then you picked it up and left quickly\n")
##        log.close()
##        return False


########END DEV SECTION#########

#Asks if dev
##dev = raw_input("Are you a developer? ")

#Initial runbefore
runbefore = False

#Creates a file
log = open("DragonGameLog.txt","a")
log.close()

#Checks if the first line is the special line
log = open("DragonGameLog.txt","r")
for line in log:
    #Updates if it's the special character
    if line == "+----------------------------------------------+\n":
        runbefore = True
        break

#If it's been run before, checks if developer
if runbefore:
    log.close()
    dragon_game()

#If it hasn't writes inital title and then checks if developer
elif not runbefore:
    log.close()
    log = open("DragonGameLog.txt","a")
    log.write("+----------------------------------------------+\n")
    log.write("+-------------PREVIOUS--ADVENTURES-------------+\n")
    log.write("+----------------------------------------------+\n")
    log.close()
    dragon_game()
