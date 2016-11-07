#Leo Ascenzi
#Hours
for h in range(24):
    #Minutes
    for m in range(60):
        #Days
        for s in range(60):
            #prints them
            print str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
