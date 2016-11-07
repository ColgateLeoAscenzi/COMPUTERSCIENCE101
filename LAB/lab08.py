#Leo Ascenzi
#Lab 07

import random

def longest_word(s):
    '''(str) -> (int)
    takes a string s and
    find the longest word
    excluding special characters
    and returns that length, int
    >>> longest_word("This is test of punc. I should'nt've taken FSEM 100")
    12
    >>> longest_word("THIS! IS! MORE! SIMPLE!")
    7
    >>> longest_word("What ifif test haha")
    4
    '''
    
    #Makes a list
    lst = s.split()
    newlst = []

    #Removes punctuation
    for word in lst:
        if word[-1] in ".,;:?":
            newlst += [word[:-1]]
        else:
            newlst += [word]
            
    #Then counts the longest word
    longestlen = 0
    for word in newlst:
        if len(word)>longestlen:
            longestlen = len(word)

    return longestlen

        

def invert_case(s):
    '''(str) -> (str)
    Takes a string s
    and returns another string
    with opposite case
    >>> invert_case("iF ONLY ONLINE GAMES HAD THIS FOR CAPS LOCK REVERSION...")
    'If only online games had this for caps lock reversion...'
    >>> invert_case("THIS IS cool!")
    'this is COOL!'
    >>> invert_case("tHE COOLEST IS THAT, IT IGNORES STUFF LIKE 123;.,?! how is this even possible?!?!?")
    'The coolest is that, it ignores stuff like 123;.,?! HOW IS THIS EVEN POSSIBLE?!?!?'
    '''
    #Adds edits the character case if it's a character only
    news = ""
    for char in s:
        #For lowercase
        if ord(char) > 96 and ord(char) < 123:
            news += chr(ord(char)-32)
        #For uppercase
        elif ord(char) > 64 and ord(char) < 91:
            news += chr(ord(char)+32)
        else:
            news += char

    return news
            


def find(s, substring, start, end):
    '''(str,str,int,int) -> (int)
    takes a string, s, substring, substring
    a start and end index, start and end, and
    finds the first index of substring in s
    >>> find("sarcasmcasmcasm","casm",0,15)
    3
    >>> find("sarcasmcasmcasm","casm",4,15)
    7
    >>> find("ababa","aba",1,5)
    2
    '''

    #Inital substring
    startidx = -1

    #Goes through consecutive slices of len(substring)
    for i in range(start,end+len(substring)):
        if substring == s[i:i+len(substring)]:
            return i
    return startidx



def multi_find(s, substring, start, end):
    '''(str,str,int,int) -> (lst)
    takes a string, s, substring, substring
    a start and end index, start and end, and
    returns a list, lst of the first indexes of
    the substring in s.
    >>> multi_find("sarcasmcasmcasm","casm",0,15)
    [3, 7, 11]
    >>> multi_find("sarcasmcasmcasm","casm",4,15)
    [7, 11]
    >>> multi_find("ababbaababababababababa","aba",0,25)
    [0, 6, 8, 10, 12, 14, 16, 18, 20]
    '''
    #Uses the find function to help solve the problem (required by problem)
    if substring in s:
        idxlst = [find(s,substring,start,end)]

        idxlst2= []

        #Goes through consecutive slices of len(substring) and finds
        for i in range(start,end+len(substring)):
            if substring == s[i:i+len(substring)]:
                idxlst2 += [i]

        #Removes the repeat    
        i = 0
        for item in idxlst2:
            if i > 0:
                idxlst += [item]
            i += 1
    else:
        idxlst = []

    return idxlst

def slice_out(s, sub):
    '''(str) -> (str)
    takes a string str
    and slices out every
    substring, sub, then
    returns the ammended string
    >>> slice_out("'And I want you to know before I die, I hid the gold in McGregory'","McGregory")
    "'And I want you to know before I die, I hid the gold in '"
    >>> slice_out("I put the care in careful", "care")
    'I put the  in ful'
    >>> slice_out("Sfootefootcrefoott mefootssafootgfoote","foot")
    'Secret message'
    '''
    news = ""
    search = 0
    idx = multi_find(s,sub,0,len(s)-1)
    if sub in s:
        #componsation for idx[search] being out of range
        for i in range(len(s)):
            idx += [0]
            
        #If it's not an empty list
        if idx != []:
            for i in range(len(s)):
                #Tests if the currint i which indexes the string, is in the forbidden index range
                if i not in range(idx[search],idx[search]+len(sub)):
                    news += s[i]
                    #Updates the forbidden index area
                    if i == idx[search]+len(sub):
                        search += 1



        
        else:
            news = s
    else:
        news = s

    return news
    

def flip_streak(flips):
    '''(int) -> (output)
    Takes the and int, flips
    and prints out the number results
    of a coin flip and the longest
    streak of flips
    >>> flip_streak(5)
    Flip results: H T T T T 
    Longest streak: 4 Tails(s)
    >>> flip_streak(10)
    Flip results: H H H H T T H H T H 
    Longest streak: 4 Head(s)
    >>> flip_streak(25)
    Flip results: T T T H T T H H H H H T T H H H T H T T T T T T T 
    Longest streak: 7 Tails(s)
    '''
    #Randomly generates H or T and adds it to results
    options = "HT"
    results = ""
    condensed = ""
    for num in range(flips):
        flip = options[random.randint(0,1)]
        results += flip + " "
        condensed += flip
        

    print "Flip results:",results

    #Creates two lists of the streaks for H and T
    longestheadsstreak = 0
    longesttailsstreak = 0
    
    hlst = condensed.strip().split("T")
    tlst = condensed.strip().split("H")

    #Measures the longest streak of H
    for streak in hlst:
        if len(streak)>longestheadsstreak:
            longestheadsstreak = len(streak)

    #Also measures the longest streak of T
    for streak in tlst:
        if len(streak)>longesttailsstreak:
            longesttailsstreak = len(streak)

    if longestheadsstreak > longesttailsstreak:
        print "Longest streak:", longestheadsstreak, "Head(s)"
    elif longesttailsstreak > longestheadsstreak:
         print "Longest streak:", longesttailsstreak, "Tails(s)"
    else:
        print "Longest streak:", longesttailsstreak, "Head(s) and Tail(s)"
     
