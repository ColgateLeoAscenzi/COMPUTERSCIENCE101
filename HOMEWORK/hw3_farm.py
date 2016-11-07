# ----------------------------------------------------------
# --------               PROGRAM 2                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 0.5
# Collaborators and sources:
#   (List any collaborators or sources here.)

# ----------------------------------------------------------
#Revision 4:
#Removed global variable
#Removed %s
#Condensed functions


#Gathers a farmer name and integer, then runs the addition process of the song lyrics to a string. then prints
def main():
    songtext = ""
    fname = raw_input("What is the farmers name? ")
    numanim = int(raw_input("How many different animals does " + fname + " keep on the farm? "))
    for animal in range(numanim):
                           aname = raw_input("Enter the name of animal " + str(animal+1) + ": ")
                           sound = raw_input("Enter the noise of animal " + str(animal+1) + ": ")
                           songtext += ("\n")
                           songtext += (fname + " had a farm, E-I-E-I-O." + "\n")
                           songtext += ("And on that farm he had a " + aname + " E-I-E-I-O." + "\n")
                           songtext += ("With a " + sound + " " + sound + " here and a " + sound + " " + sound + " there" + "\n")
                           songtext += ("Here a " + sound + " there a " + sound + " everywhere a " + sound + " " + sound + "\n")
                           songtext += (fname + " had a farm, E-I-E-I-O." + "\n")
    print songtext
                           
#Runs program
main()





