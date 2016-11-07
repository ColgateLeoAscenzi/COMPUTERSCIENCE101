# ----------------------------------------------------------
# HW 6, Program 2
# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Leo Ascenzi
# Hours spent on this program: 0.1
# Collaborators and sources: None
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


def convert(x):
    '''(str) -> (str or float or int)
    Takes a string, x, and returns a
    string float or int depending on logic
    >>> type(convert("hello"))
    <type 'str'>
    >>> type(convert("42.9001"))
    <type 'float'>
    >>> type(convert("7"))
    <type 'int'>
    '''
    #Checks if x has alphabetic characters
    if x.isalpha():
        return x

    #Otherwise if it has a period
    elif x.count(".") > 0:
        return float(x)

    #And if not then it's an int
    else:
        return int(x)


def str_to_list(x):
    '''(str) -> (lst)
    Takes a string, x, and
    converts it into a list
    of items that were in x
    seperated by a comma
    >>> str_to_list("I, once, was, str, but, now, am, list")
    ['I', ' once', ' was', ' str', ' but', ' now', ' am', ' list']
    >>> str_to_list("Amazing python, how sweet the code")
    ['Amazing python', ' how sweet the code']
    >>> str_to_list("John Newton, 1725, 1807")
    ['John Newton', ' 1725', ' 1807']
    '''
    x_list = x.split(",")
    return x_list



###TEST CASES (write additional test cases)
##a = "apple"
##b = "3"
##c = "7.9"
##d = "hello"
##e = "world"
##r = "99"
##abc = a+","+b+","+c
##der = d+","+e+","+r
##
##print a, "is a", type(convert(a))
##print b, "is a", type(convert(b))
##print c, "is a", type(convert(c))
##print d, "is a", type(convert(d))
##print e, "is a", type(convert(e))
##print r, "is a", type(convert(r))
##
##print abc, "-->", str_to_list(abc)
##print der, "-->", str_to_list(der)
##
##apple is a <type 'str'>
##3 is a <type 'int'>
##7.9 is a <type 'float'>
##hello is a <type 'str'>
##world is a <type 'str'>
##99 is a <type 'int'>
##apple,3,7.9 --> ['apple', '3', '7.9']
##hello,world,99 --> ['hello', 'world', '99']
