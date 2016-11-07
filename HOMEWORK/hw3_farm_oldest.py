# ----------------------------------------------------------
# --------               PROGRAM 2                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 1
# Collaborators and sources:
#   (List any collaborators or sources here.)

# ----------------------------------------------------------

#Collection
animals = ""
sounds = ""
animallength = ""
soundslength = ""

#Gets preliminary data
fname = raw_input("What is ther farmers name? ")
numanim = int(raw_input("How many different animals does %s keep on the farm? " %fname))

#Animal Control Collects Animals
def animalcontrol(nameanim):
    global animals
    animals  = animals + nameanim + "."
    
#Microphone Collects Sounds
def microphone(soundanim):
    global sounds
    sounds = sounds + soundanim + ","

#Collects stuff to empty strings
def collection():
    for Tiere in range(numanim):
        tempname = raw_input("Enter the name of animal %s: " % (Tiere+1))
        tempsound = raw_input("Enter the noise of animal %s: " % (Tiere+1))
        #Calls animal control to capture animal
        animalcontrol(tempname)
        #Utilizes microphone to record sound
        microphone(tempsound)

#Plays stuff
def indexing():
    for Tiere in range(numanim):
        print
        print fname, "had a farm, E-I-E-I-O."
        print "And on that farm he had a", cutlets[Tiere], "E-I-E-I-O."
        print "With a", stutters[Tiere], stutters[Tiere], "here and a", stutters[Tiere], stutters[Tiere], "there"
        print "Here a", stutters[Tiere], "there a", stutters[Tiere], "everywhere a", stutters[Tiere], stutters[Tiere]
        print fname, "had a farm, E-I-E-I-O."
        print
    
#Does everything
def main():
    global cutlets
    global stutters
    collection()
    #When animals are split they become cutlets
    cutlets = animals.split(".")
    #When sounds are broken they become stutters
    stutters = sounds.split(",")
    indexing()


main()


