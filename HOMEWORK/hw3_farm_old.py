# ----------------------------------------------------------
# --------               PROGRAM 2                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 0.16666666666
# Collaborators and sources:
#   (List any collaborators or sources here.)

# ----------------------------------------------------------
#Gets farmer name and number
songtext = ""
fname = raw_input("What is the farmers name? ")
numanim = int(raw_input("How many different animals does %s keep on the farm? " % fname))

#A function to add things to a previously created empty string
def addition(fname, aname, sound):
    '''(str, str, str) -> (str)
    Uses three strings to build a composite phrase
    >>>marutin, pig, oink
    marutin had a farm, E-I-E-I-O.
    And on that farm he had a pig E-I-E-I-O.
    With a oink oink here and a oink oink there
    Here a oink there a oink everywhere a oink oink
    marutin had a farm, E-I-E-I-O.
    '''
    global songtext
    songtext = songtext + ("\n")
    songtext = songtext + (fname + " had a farm, E-I-E-I-O." + "\n")
    songtext = songtext + ("And on that farm he had a " + aname + " E-I-E-I-O." + "\n")
    songtext = songtext + ("With a " + sound + " " + sound + " here and a " + sound + " " + sound + " there" + "\n")
    songtext = songtext + ("Here a " + sound + " there a " + sound + " everywhere a " + sound + " " + sound + "\n")
    songtext = songtext + (fname + " had a farm, E-I-E-I-O." + "\n")

#For eacha animal calls the addition of the animal and sound to the string
def main():
    global fname
    for animal in range(numanim):
                           tempname = raw_input("Enter the name of animal %s: " % (animal+1))
                           tempsound = raw_input("Enter the noise of animal %s: " % (animal+1))
                           addition(fname, tempname, tempsound)
    print songtext
                           
#Runs program
main()





