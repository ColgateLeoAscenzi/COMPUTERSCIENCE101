# ----------------------------------------------------------
# HW 6, Program 1
# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Leo Ascenzi
# Hours spent on this program: 0.5
# Collaborators and sources: Type(Collaborators)= <type 'bool'>
# >>> print Collaborators
# False
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


def valid_email(email):
    '''(str) -> (bool)
    takes a string, email, and
    tests if the string is a valid
    email then returns a boolean
    >>> valid_email("@colgate")
    False
    >>> valid_email("colgate@")
    False
    >>> valid_email("c@o@l@g@t@e@")
    False
    >>> valid_email("valid@email.com")
    True
    '''
    #First checks if there's only 1 at
    atcount = email.count("@")
    if atcount != 1:
        return False
    else:
        #next checks if the two segments are empty or not
        emailsegments = email.split("@")
        return len(emailsegments[0])>0 and len(emailsegments[1])>0
        
    


def unsubscribe():
    '''(None) -> (lst)
    Takes no input except
    raw_input then returns
    a list of emails to remove
    '''
    remove = []
    while True:
        tempemail = raw_input("Enter an email address to unsubscribe (or 'done' to exit): ")
        if tempemail == "done":
            print len(remove), "email addresses will be removed."
            print
            break
        else:
            if valid_email(tempemail):
                remove += [tempemail]
                print tempemail, "will be removed."
                print
            else:
                invalid = True
                while invalid:
                    tempemail2 = raw_input("Invalid email address, try again: ")
                    if valid_email(tempemail2):
                        break
                remove += [tempemail2]
                print tempemail2, "will be removed."
                print

        
            
    return remove



###TEST CASES (write additional test cases)
##a = "a@b.c"
##b = "mesmith@colgate.edu"
##c = "computer_science"
##d = "lascenzi@colgate.edu"
##e = "hello@world@com"
##f = "@ascenzi"
##g = "ascenzi@"
##
##print a, "is a valid email address:", valid_email(a)
##print b, "is a valid email address:", valid_email(b)
##print c, "is a valid email address:", valid_email(c)
##print d, "is a valid email address:", valid_email(d)
##print e, "is a valid email address:", valid_email(e)
##print f, "is a valid email address:", valid_email(f)
##print g, "is a valid email address:", valid_email(g)



##>>> remove = unsubscribe()
##Enter an email address to unsubscribe (or 'done' to exit): mader-line@
##Invalid email address, try again: mader-line@colgate
##mader-line@colgate will be removed.
##
##Enter an email address to unsubscribe (or 'done' to exit): gh@fmail.com
##gh@fmail.com will be removed.
##
##Enter an email address to unsubscribe (or 'done' to exit): @darius
##Invalid email address, try again: darius@
##Invalid email address, try again: darius@cornell.org
##darius@cornell.org will be removed.
##
##Enter an email address to unsubscribe (or 'done' to exit): done

##3 email addresses will be removed.
##>>> print remove
##['mader-line@colgate', 'gh@fmail.com', 'darius@cornell.org']

unsubscribe()
