# ----------------------------------------------------------
# HW 5, Part 1 
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent in total:   2.25(2 hours are slice67)
# Collaborators (if any) and resources used (if any):  
# Feedback: What was the hardest part of this assignment?
#   slice67(L)
# Feedback: Any suggestions for improving the assignment?	
#   A big suggestion, give a hint for the harder prolems
#   like slice67 took me 2 hours to solve (I timed it)
#   whereas no_teen_sum and fix_teen took me 1 min 27 seconds (I timed it aswell)
# ----------------------------------------------------------

#1? byebye13?
def sum13(L):
    '''(L) -> (num)
    Sums the numbers in a list L
    except for the where 13 = -1 and
    the number after 13 = 0.
    >>> sum13([13,13,13,4])
    -2
    >>> sum13([1,2,3,4,5,6,7,8,9,10,11,12,13])
    77
    >>> sum13([12,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13])
    3
    '''
    #initializes a count and sum
    i = 0
    sum = 0
    #Will end after all items
    while i < len(L):
        #If it's not lucky #13 then do the regular addition
        if L[i]!=13:
            sum += L[i]
            i += 1
        #Otherwise treat it as -1 and skip the next one by adding 2 to the count
        else:
            sum += -1
            i += 2
    return sum

#2? cut3to4?
#ATTENTION
#slice67([7,3,1,3,1,4,1,4,10])
#returns [7, 1, 4, 10]
#because the first 3 to 4 slices out the second 3.
#thus the last 4 only counts as a lone 4, and not
#part of a 3-4 slice
def slice67(L):
    '''(L) -> (L)
    Takes a list L and removes the
    numbers between 3 and 4
    including 3 and 4 themselves
    assumes every 3 has at least
    one four following it
    >>> slice67([4,3,4])
    [4]
    >>> slice67([7,3,1,3,1,4,1,4,10])
    [7, 1, 4, 10]
    >>> slice67([3,1,4,4,2,3,4])
    [4, 2]
    '''
    #New list
    L2 = []
    #Starts out looking for a 3 but not a 4
    lookfor3 = True
    lookfor4 = False
    #Loops over the indexes in L
    for i in range(len(L)):
        #Handles 3 logic, essentially if it's looking for a 3 and finds ones
        #it starts to cut and look for the ending 4. If it's looking for a 3
        #but doesn't find one, it adds that to the L2
        if L[i] == 3 and lookfor3:
            lookfor3 = False
            lookfor4 = True
        elif L[i] != 3 and lookfor3:
            L2+= [L[i]]

        #Handles 4 logic, if it's looking for the 4 then it wont add to L2
        #Unless it finds the 4, the it will look for another 3, but wont
        #add the 4 to the list. And if it's not looking for a 4 but finds
        #a 4 it adds that to the list as that 4 is seperate from the 3-4
        #section
        elif L[i] == 4 and lookfor4:
            lookfor3 = True
            lookfor4 = False
        elif L[i] == 4 and not lookfor4:
            L2 += [L[i]]
        elif L[i] != 4 and lookfor4:
            pass

        #Just incase         
        else:
            L2 += [L[i]]
            
    return L2

        
            
        
    
#3
def no_teen_sum(a, b, c):
    '''(int, int, int) -> (int)
    takes three integers, int, and sums
    them
    >>> no_teen_sum(12,3,13)
    15
    >>> no_teen_sum(15,15,16)
    46
    >>> no_teen_sum(13,17,19)
    0
    '''
    #Sums these numbers
    sum = fix_teen(a)+fix_teen(b)+fix_teen(c)
    return sum
    
#3? adjust_teen?
def fix_teen(n):
    '''(int) -> (int)
    takes an integer, int and changes
    it to - if it's a teen, unless it's 15
    or 16
    >>> fix_teen(15)
    15
    >>> fix_teen(13)
    0
    >>> fix_teen(100000)
    100000
    '''
    #If it's a teen (which doesn't mean 15 or 16) it's now 0
    if n==13 or n==14 or n==17 or n==18 or n==19:
        n = 0
    return n
#4
def double_reverse(L):
    '''(list) -> (list)
    takes a list L of strings
    and reverses the
    order of the items in the list
    and the letters of each item
    >>> double_reverse(["what", "even", "is", "this"])
    ['siht', 'si', 'neve', 'tahw']
    >>> double_reverse(["racecar", "r", "racecar"])
    ['racecar', 'r', 'racecar']
    >>> double_reverse(["test", "list", "please", "ignore"])
    ['erongi', 'esaelp', 'tsil', 'tset']
    '''
    #Makes a list for the string reversal
    Ls = []
    #Reverses each string in the list
    for item in list(L):
        Ls += [string_reverse(item)]

    #Makes a list for string reversal
    Lr = []
    #Reverses list
    topnum = len(L)-1
    for i in range(len(L)):
        Lr += [Ls[(topnum-i)]]
    return Lr
        

def string_reverse(s):
    '''(str) -> (str)
    takes a string s and reverses
    the order of the letters in the
    string
    >>> string_reverse("slice67 is so hard")
    'drah os si 76ecils'
    >>> string_reverse("ysae saw melborp siht")
    'this problem was easy'
    >>> string_reverse("racecar")
    'racecar'
    '''
    news = ""
    topnum = len(s)-1
    for i in range(len(s)):
        news += s[(topnum-i)]
    return news
    
#Challenge 2
def xyz_there(s):
    '''fill in this docstring!
    '''
#5 tagify?
def make_tag_list(text, lst):
    '''(str, list) -> (list)
    takes a tag str and a list lst
    made of strings
    and creates a new list with the
    tags and strings
    >>> make_tag_list("head", ["Welcome to the World Wide Web"])
    ['<head>Welcome to the World Wide Web</head>']
    >>> make_tag_list("i", ["Italics", "add", "emphasis!"])
    ['<i>Italics</i>', '<i>add</i>', '<i>emphasis!</i>']
    make_tag_list("tbody", ["<tr>Hello</tr>", "<tr>World</tr>"])
    ['<tbody><tr>Hello</tr></tbody>', '<tbody><tr>World</tr></tbody>']
    '''
    newlst = []
    opentag = "<" + text + ">"
    closetag = "</" + text + ">"
    for item in lst:
        newlst += [opentag + item + closetag]
    return newlst

#Challenge 1
def make_bricks(small, big, goal):
    '''fill in this docstring!
    '''

# you need to write tests, i.e. function calls
# for each function


# you do not need to write a main function
# for this homework.
