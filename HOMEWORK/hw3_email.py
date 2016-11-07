# ----------------------------------------------------------
# --------               PROGRAM 1                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 0.25 
# Collaborators and sources: Me, Myself and I
#   (List any collaborators or sources here.)
# With one exam and several homeworks completed, how is the 
# course going for you so far?
#   (: So far so good. I came to Colgate thinking I would major
#    in physics and already this course has changed my mind! :)
# ----------------------------------------------------------

while True:
    #Gets input
    email = raw_input("Enter an email: ")

#First checks if email is from colgate
    if "colgate.edu" in email:
        if "@" in email:
            #breaks it into segments
            seg = email.split('@')
            #if there are only two parts, and the first half isn't empty
            if len(seg) == 2 and len(seg[0]) != 0:
                #and if the second half isn't empty
                if  len(seg[1]) != 0:
                    #Then display the email
                    print "Valid email"
                    print "Local part:", seg[0]
                    print "Domain part:", seg[1]
                    #because why not
                    print "From COLGATE!"
        #Otherwise annoy the user by not telling why it's invalid
                else:
                    print "Invalid email"
            else:
                print "Invalid email"
        else:
            print "Invalid email"


#If email not from colgate, then checks the actual validity of the email
    else:
        #first case for invalid email, no @
        if "@" in email:
            seg = email.split('@')
            if len(seg) == 2 and len(seg[0]) != 0:
                if  len(seg[1]) != 0:
                    print "Valid email"
                    print "Local part:", seg[0]
                    print "Domain part:", seg[1]
                else:
                    print "Invalid email"
            else:
                print "Invalid email"
        else:
            print "Invalid email"

    print

    
