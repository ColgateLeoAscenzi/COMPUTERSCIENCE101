# ----------------------------------------------------------
# HW 5, Part 2 
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent in total:  1
# Collaborators (if any):  
# Feedback: Having completed this assignment, do you feel 
# like you understand how functions work and how to define 
# them?
#   Yes
# Feedback: What did you do over fall break?
#   I visited my friend who goes to UNC-Chapel Hill
#   As well as my family briefly. I got to restock
#   on hangers from my closet (a gift of my mom)
#   and eat delicious home cooked meals. I also decided
#   that the food in Frank is way better than the food
#   in the cafeteria of UNC-CH (Lenoir specifically)
# ----------------------------------------------------------
def remove_single(str, chr):
    '''(str, str) -> (str)
    takes a string str and removes
    the first occurance of string
    chr in the str.
    >>>remove_single("anagram", "a")
    nagram
    >>>remove_single("anagram", "m")
    m
    >>>remove_single("he llo", " ")
    hello
    '''
    lookforchr = True
    news = ""
    for i in range(len(str)):
        if str[i] == chr and not lookforchr:
                   news += str[i]
        elif str[i] == chr and lookforchr:
                   lookforchr = False
        else:
                   news+= str[i]

    return news
            

def is_anagram(word1,word2):
    '''(str, str) -> (bool)
    checks if word1 and word2
    are anagrams and returns
    a boolean
    >>> is_anagram("banana", "cow")
    False
    >>> is_anagram("banana", "banono")
    False
    >>> is_anagram("banana", "bannaa")
    True
    '''
#Word Setup Half
    #Initial Counts
    space1 = 0
    space2 = 0
    
    #Counts the spaces
    for chr in word1:
        if chr == " ":
            space1 += 1
    for chr in word2:
        if chr == " ":
            space2 += 1
            
    #Secondary Initial Counts
    i = 0
    j = 0

    #Removes the spaces
    while i < space1:
        word1 = remove_single(word1, " ")
        i += 1
    while j < space2:
        word2 = remove_single(word2, " ")
        j += 1
        
#Anagram Checking Half (And because I assume I can't just use sorted()
#If I could use sorted I would do if sorted(word1) == sorted(word2): return True else: return False
    lettercount1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lettercount2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if len(word1) == len(word2):
        #Makes list of letter counts in word1
        for ltr in word1:
            #Tests if letter is uppercase and counts the occurances in a list
            if ltr == "A":
                lettercount1[0] += 1
            elif ltr == "B":
                lettercount1[1] += 1
            elif ltr == "C":
                lettercount1[2] += 1
            elif ltr == "D":
                lettercount1[3] += 1
            elif ltr == "E":
                lettercount1[4] += 1
            elif ltr == "F":
                lettercount1[5] += 1
            elif ltr == "G":
                lettercount1[6] += 1
            elif ltr == "H":
                lettercount1[7] += 1
            elif ltr == "I":
                lettercount1[8] += 1
            elif ltr == "J":
                lettercount1[9] += 1
            elif ltr == "K":
                lettercount1[10] += 1
            elif ltr == "L":
                lettercount1[11] += 1
            elif ltr == "M":
                lettercount1[12] += 1
            elif ltr == "N":
                lettercount1[13] += 1
            elif ltr == "O":
                lettercount1[14] += 1
            elif ltr == "P":
                lettercount1[15] += 1
            elif ltr == "Q":
                lettercount1[16] += 1
            elif ltr == "R":
                lettercount1[17] += 1
            elif ltr == "S":
                lettercount1[18] += 1
            elif ltr == "T":
                lettercount1[19] += 1
            elif ltr == "U":
                lettercount1[20] += 1
            elif ltr == "V":
                lettercount1[21] += 1
            elif ltr == "W":
                lettercount1[22] += 1
            elif ltr == "X":
                lettercount1[23] += 1
            elif ltr == "Y":
                lettercount1[24] += 1
            elif ltr == "Z":
                lettercount1[25] += 1
                
            #Tests if there are lower case letters
            if ltr == "a":
                lettercount1[26] += 1
            elif ltr == "b":
                lettercount1[27] += 1
            elif ltr == "c":
                lettercount1[28] += 1
            elif ltr == "d":
                lettercount1[29] += 1
            elif ltr == "e":
                lettercount1[30] += 1
            elif ltr == "f":
                lettercount1[31] += 1
            elif ltr == "g":
                lettercount1[32] += 1
            elif ltr == "h":
                lettercount1[33] += 1
            elif ltr == "i":
                lettercount1[34] += 1
            elif ltr == "j":
                lettercount1[35] += 1
            elif ltr == "k":
                lettercount1[36] += 1
            elif ltr == "l":
                lettercount1[37] += 1
            elif ltr == "m":
                lettercount1[38] += 1
            elif ltr == "n":
                lettercount1[39] += 1
            elif ltr == "o":
                lettercount1[40] += 1
            elif ltr == "p":
                lettercount1[41] += 1
            elif ltr == "q":
                lettercount1[42] += 1
            elif ltr == "r":
                lettercount1[43] += 1
            elif ltr == "s":
                lettercount1[44] += 1
            elif ltr == "t":
                lettercount1[45] += 1
            elif ltr == "u":
                lettercount1[46] += 1
            elif ltr == "v":
                lettercount1[47] += 1
            elif ltr == "w":
                lettercount1[48] += 1
            elif ltr == "x":
                lettercount1[49] += 1
            elif ltr == "y":
                lettercount1[50] += 1
            elif ltr == "z":
                lettercount1[51] += 1
                
        #Makes list of letter count for word 2
        for ltr in word2:
            #Tests if letter is uppercase and counts the occurances in a list
            if ltr == "A":
                lettercount2[0] += 1
            elif ltr == "B":
                lettercount2[1] += 1
            elif ltr == "C":
                lettercount2[2] += 1
            elif ltr == "D":
                lettercount2[3] += 1
            elif ltr == "E":
                lettercount2[4] += 1
            elif ltr == "F":
                lettercount2[5] += 1
            elif ltr == "G":
                lettercount2[6] += 1
            elif ltr == "H":
                lettercount2[7] += 1
            elif ltr == "I":
                lettercount2[8] += 1
            elif ltr == "J":
                lettercount2[9] += 1
            elif ltr == "K":
                lettercount2[10] += 1
            elif ltr == "L":
                lettercount2[11] += 1
            elif ltr == "M":
                lettercount2[12] += 1
            elif ltr == "N":
                lettercount2[13] += 1
            elif ltr == "O":
                lettercount2[14] += 1
            elif ltr == "P":
                lettercount2[15] += 1
            elif ltr == "Q":
                lettercount2[16] += 1
            elif ltr == "R":
                lettercount2[17] += 1
            elif ltr == "S":
                lettercount2[18] += 1
            elif ltr == "T":
                lettercount2[19] += 1
            elif ltr == "U":
                lettercount2[20] += 1
            elif ltr == "V":
                lettercount2[21] += 1
            elif ltr == "W":
                lettercount2[22] += 1
            elif ltr == "X":
                lettercount2[23] += 1
            elif ltr == "Y":
                lettercount2[24] += 1
            elif ltr == "Z":
                lettercount2[25] += 1
                
            #Tests if there are lower case letters
            if ltr == "a":
                lettercount2[26] += 1
            elif ltr == "b":
                lettercount2[27] += 1
            elif ltr == "c":
                lettercount2[28] += 1
            elif ltr == "d":
                lettercount2[29] += 1
            elif ltr == "e":
                lettercount2[30] += 1
            elif ltr == "f":
                lettercount2[31] += 1
            elif ltr == "g":
                lettercount2[32] += 1
            elif ltr == "h":
                lettercount2[33] += 1
            elif ltr == "i":
                lettercount2[34] += 1
            elif ltr == "j":
                lettercount2[35] += 1
            elif ltr == "k":
                lettercount2[36] += 1
            elif ltr == "l":
                lettercount2[37] += 1
            elif ltr == "m":
                lettercount2[38] += 1
            elif ltr == "n":
                lettercount2[39] += 1
            elif ltr == "o":
                lettercount2[40] += 1
            elif ltr == "p":
                lettercount2[41] += 1
            elif ltr == "q":
                lettercount2[42] += 1
            elif ltr == "r":
                lettercount2[43] += 1
            elif ltr == "s":
                lettercount2[44] += 1
            elif ltr == "t":
                lettercount2[45] += 1
            elif ltr == "u":
                lettercount2[46] += 1
            elif ltr == "v":
                lettercount2[47] += 1
            elif ltr == "w":
                lettercount2[48] += 1
            elif ltr == "x":
                lettercount2[49] += 1
            elif ltr == "y":
                lettercount2[50] += 1
            elif ltr == "z":
                lettercount2[51] += 1

                
        if lettercount1 == lettercount2:
            return True
        else:
            return False
    else:
        return False

    
def main():
    '''runs the prorgams
    is_anagram
    '''
    word1 = raw_input("Enter the first word! ")
    word2 = raw_input("Enter the second word! ")
    if is_anagram(word1,word2):
        print "Yes, these are anagrams!"
    else:
        print "Sorry, these are not anagrams!"
    

main()
