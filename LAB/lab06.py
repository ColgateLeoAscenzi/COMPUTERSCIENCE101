#Leo Ascenzi

def odd_vs_even(lst):
    '''Accepts a list of integers
    and returns True if the number
    off odds matches that of evens
    and false if otherwise
    >>> odd_vs_even([1,2,3,4,5,6])
    True
    >>> odd_vs_even([3,3,3,3,3,3])
    False
    >>> odd_vs_even([2,2,2,3,3,3])
    True
    '''
    #Initializes counts
    evens=0
    odds=0
    #Checks if number is odd or even
    for num in lst:
        if num%2==0:
            evens+=1
        else:
            odds+=1
    #If counts are the same it's true
    return evens==odds

def symmetrical_list(lst):
    '''Accepts a list of integers
    and returns True if it is symmetrical
    and false if not
    >>> symmetrical_list([1,2,3,3,2,1])
    True
    >>> symmetrical_list([1,2,3,2,1])
    True
    >>> symmetrical_list([1,2,3,4,5,5,4,4,3,2,1])
    False
    '''
    #Looks in half the range because symmetry
    for i in range(len(lst)/2):
                   #Checks if each num is the same at the opposite index
                   if lst[i]!=lst[(-1*(i+1))]:
                       return False
    return True

def first_index_of(s, char):
    '''Accepts two strings s
    and char and returns the first index
    where char is first found in s
    >>> first_index_of("hello world", "l")
    2
    >>> first_index_of("hello world", "z")
    -1
    >>> first_index_of("lllllooooolllll", "o")
    5
    '''
    #Initial index is -1 just incase chr isn't in str
    idx=-1
    #breaks is chr is found
    for i in range(len(s)):
        if s[i] == char:
            idx=i
            break
    return idx


def last_index_of(s, char):
    '''Accepts two strings s
    and char and returns the last index
    where char is first found in s
    >>> last_index_of("hello world", "l")
    9
    >>> last_index_of("hello world", "z")
    -1
    >>> last_index_of("lllllooooolllll", "o")
    9
    '''
    #Initial index is -1 just incase chr isn't in str
    idx=-1
    #continues to update till last index
    for i in range(len(s)):
        if s[i] == char:
            idx=i
    return idx    

def appear_in_order_2(w, char1, char2):
    '''Accepts 3 strings w
    char1 and char2 and determines if
    char1 occurs anytime before char2
    >>> appear_in_order_2("bab","a","b")
    True
    >>> appear_in_order_2("pool","o","o")
    True
    >>> appear_in_order_2("determine","e","d")
    False
    '''
    #Checks if the first index of char1 is less than
    #the first index of char2 and returns True if True
    return first_index_of(w,char1)<last_index_of(w,char2)

def appear_in_order_3(w,char1,char2,char3):
    '''Accepts 4 strings w char1, char2 and
    char 3 and determines if char1 occurs
    somewhere before char2 and char2 occurs
    somewhere before char3
    >>> appear_in_order_3("bacb","a","b","c")
    False
    >>> appear_in_order_3('abc','a','b','c')
    True
    >>> appear_in_order_3('adcb','a','b','c')
    False
    '''
    #Checks if char1 and char2 are in order, then if char2 and char3 are in order, then if char1 is before char3, and finally if char1 is in w
    return appear_in_order_2(w,char1,char2) and appear_in_order_2(w,char2,char3) and appear_in_order_2(w,char1,char3) and char1 in w

def contiguous_sum(lst):
    '''Accepts a list lst and
    finds the largest contiguous sum
    in the list
    '''
    #Initializes the first sum as the first number
    currentsum = biggestsum = lst[0]
    
    #Searches through a range starting at the second number
    for i in range(1,len(lst)):
        #If the current number is bigger than the current sum and the current number
        if lst[i] > (currentsum + lst[i]):
            currentsum = lst[i]
        #Otherwise the add the current number
        else:
            currentsum += lst[i]

        #Updates the biggest sum if the current sum is greater than the previously biggest sum
        if currentsum > biggestsum:
            biggestsum = currentsum

    return biggestsum


    
                      
