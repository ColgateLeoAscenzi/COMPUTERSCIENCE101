import random
import time

#1
def username_generator(first, last):
    '''(str, str) -> str
    This function takes first and last and
    combines them into one username with
    the first letter of the first name
    and at max the last 5 letters of the
    last name
    >>>username_generator("Albert", "Einstein")
    aeinst
    >>>username_generator("John", "Doe")
    jdoe
    >>>username_generator("Leonardo", "Ascenzi")
    lascen
    '''
    #Creates initial empty username string
    username = ""

    #Converts upper to lower
    firstlow = first.lower()
    lastlow = last.lower()
    
    #Checks if last name is 5 letters or more
    if len(last)>4:
        username += firstlow[0] + lastlow[0:5]
        return username
    else:
        username += firstlow[0] + lastlow
        return username

    
#2  
def substring_count(s, substr):
    '''(str, str) -> int
    This function takes a string (s)
    and a 3 letter substring (substr)
    and returns how many times the
    substring was found in the string
    with overlaps included
    >>>substring_count("Hello World", "hello")
    Substring Must Be 3 Letters
    >>>substring_count("Hallo Erde", "hel")
    0
    >>>substring_count("lolololololol", "lol")
    6
    '''
    #Sets an initial count
    count = 0
    #Makes sure substring is 3 characters
    if len(substr)!=3:
        print "Substring Must Be 3 Letters"
    else:
        #Range is -2 because it needs to account for range +2 later
        for num in range(len(s)-2):
            #Checks if the string at index num is the same as the character in the substring and consecutive ones
            if s[num] == substr[0] and s[(num+1)] == substr[1] and s[(num+2)] == substr[2]:
                count += 1
            else:
                pass
        return count

#3
def catdog(s):
    '''(str) -> bool
    This function takes a string and returns
    true if 'cat' and 'dog' appear the same
    number of times as long as they appear
    at least once
    >>> catdog("CATDOGdogdOgcatcatCaTDOg")
    True
    >>> catdog("c4td0g")
    False
    >>> catdog("cats aren't better than dogs")
    True
    '''
    catcount = 0
    dogcount = 0
    news = s.lower()
    if 'cat' in news and 'dog' in news:
        #Counts Cats
        for num1 in range(len(news)-2):
            #Checks if the string at index num is the same as the character in the substring and consecutive ones
            if news[num1] == "c" and news[(num1+1)] == "a" and news[(num1+2)] == "t":
                catcount += 1

        #Counts Dogs
        for num in range(len(news)-2):
            #Checks if the string at index num is the same as the character in the substring and consecutive ones
            if news[num] == "d" and news[(num+1)] == "o" and news[(num+2)] == "g":
                dogcount += 1

        if catcount == dogcount:
            return True
        
        else:

            return False
        
         
    else:
        return False

#4
def throw_die():
    '''None)
    This function doesn't take an argument
    generates random number from 1 to 6
    >>>throw_die()
    2
    >>>throw_die()
    1
    >>>throw_die()
    6
    '''
    #Generates a random integer between 1 and 6
    num = random.randint(1,6)
    return num

#5
def count_snake_eyes(n):
    '''(int) -> int
    This function takes an integer and
    counts the number of times snake eyes
    are rolled (double 1's) then it returns
    the number of snake eyes rolled
    >>>count_snake_eyes(100)
    3
    >>> count_snake_eyes(10000)
    264
    >>> count_snake_eyes(1)
    0
    '''
    count = 0
    snakes = 0
    #Sets up a loop
    while True:
        #That breaks when the number of specified rolls has been reached
        if count == n:
            return snakes
            break
        #Otherwise it runs and rolls the dice twice
        else:
            temp1 = throw_die()
            temp2 = throw_die()
            #Records if the dice are 1 and 1
            if temp1 == temp2 and temp1 == 1:
                snakes += 1
                count += 1
            #Counts as a throw
            else:
                count += 1

#6
def run_snake_eyes():
    '''(none) -> float
    This function takes no argument
    but asks for an integer and then
    returns the fraction of times
    snake eyes was rolled
    >>> run_snake_eyes()
    How many times would you like to throw a pair of dice? 1
    The fraction of times we threw snake eyes was 0.0
    >>> run_snake_eyes()
    How many times would you like to throw a pair of dice? 1000
    The fraction of times we threw snake eyes was 0.033
    >>> run_snake_eyes()
    How many times would you like to throw a pair of dice? 100000
    The fraction of times we threw snake eyes was 0.02771
    '''
    n = int(raw_input("How many times would you like to throw a pair of dice? "))
    print "The fraction of times we threw snake eyes was", (float(count_snake_eyes(n))/n)

#7       
def anagram_generator(word):
    '''(str) -> (str)
    This function takes a string as
    an argument and randomizes the letters
    then spits it back out
    >>> anagram_generator("hello")
    'olleh'
    >>> anagram_generator("hello")
    'hlole'
    >>> anagram_generator("hello")
    'heoll'
    '''
    #Sets up counts and empty strings
    count = 0
    randnums = ""
    anagram = ""
    length = len(word)

    #Makes a loop that breaks after a string of len(word) random numbers is generated that do not repeat
    while True:
        temp = str(random.randint(0,(len(word)-1)))
        if count == length:
            break
        else:
            if temp in randnums:
                pass
            else:
                randnums += temp
                count += 1
                
    #Makes a loop that takes the random number index of the word and adds it to a new string         
    for chr in randnums:
        anagram += word[int(chr) ]

    #Returns the anagram
    return anagram




#Fun Statistics
def repeat(what):
    count = 0
    while True:
        real = what
        temp = anagram_generator(what)
        if real == temp:
            return count
            break
        else:
            count += 1

def thousand_average(what):
    summ = 0
    for i in range(100000):
        summ += int(repeat(what))
    return summ/float(100000)
start = time.clock()
print thousand_average("1")
elasped1 = (time.clock()-start)
print elasped1
print thousand_average("12")
elasped2 = (time.clock()-start)
print elasped2
print thousand_average("123")
elasped3 = (time.clock()-start)
print elasped3
print thousand_average("1234")
elasped4 = (time.clock()-start)
print elasped4
print thousand_average("12345")
elasped5 = (time.clock()-start)
print elasped5
print thousand_average("123456")
elasped6 = (time.clock()-start)
print elasped6
print thousand_average("1234567")
elasped7 = (time.clock()-start)
print elasped7

























    
