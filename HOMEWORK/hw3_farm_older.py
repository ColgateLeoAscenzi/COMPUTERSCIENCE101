# ----------------------------------------------------------
# --------               PROGRAM 2                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 4
# Collaborators and sources:
#   (List any collaborators or sources here.)

# ----------------------------------------------------------
#Collection
animals = ""
sounds = ""
animallength = ""
soundslength = ""
count1 = 0
count2 = 0

#Gets preliminary data
fname = raw_input("What is ther farmers name? ")
numanim = int(raw_input("How many different animals does %s keep on the farm? " %fname))

#Animal Control Collects Animals
def animalcontrol(nameanim):
    global animals
    global animallength
    animals  = animals + nameanim
    animallength = animallength + str(len(nameanim))
    
#Microphone Collects Sounds
def microphone(soundanim):
    global sounds
    global soundslength
    sounds = sounds + soundanim
    soundslength = soundslength + str(len(soundanim))

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
        global count1
        global count2
        for i in range(numanim):
                temp1 = int(animallength[i])+count1
                temp2 = int(soundslength[i])+count2
                print
                print fname, "had a farm, E-I-E-I-O."
                
                print "And on that farm he had a", animals[(count1):(temp1)], "E-I-E-I-O."
                
                print "With a", sounds[(count2):(temp2)], sounds[(count2):(temp2)], "here and a",
                print sounds[(count2):(temp2)], sounds[(count2):(temp2)], "there"
                
                print "Here a", sounds[(count2):(temp2)], "there a", sounds[(count2):(temp2)], "everywhere a",
                print sounds[(count2):(temp2)], sounds[(count2):(temp2)]
                
                print fname, "had a farm, E-I-E-I-O."
                print
                
                count1 = count1 + int(animallength[i])
                count2 = count2 + int(soundslength[i])

    
#Does everything
def main():
    collection()
    indexing()


main()





