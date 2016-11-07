# ----------------------------------------------------------
# --------               PROGRAM 3                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on this program: 0.66
# Collaborators and sources:
#   (List any collaborators or sources here.)

# ----------------------------------------------------------

def is_leap_year(y):
        if y%4 == 0:
                return True
        else:
                return False
#Anything under 1582 is invalid
invalidrange = range(1582)

#defines start and endyears for future rearranging
startyear = 0
endyear = 0


def main():
        #gets inputs
        year1 = int(raw_input("Enter a year: "))
        year2 = int(raw_input("Enter a second year: "))
        #checks valid range
        if year1 in invalidrange or year2 in invalidrange:
                print "The range must start after or at 1582"

        #checks which year is bigger        
        else:
                if year1>year2:
                        startyear = year2
                        endyear = year1
                elif year2>year1:
                        startyear = year1
                        endyear = year2
                else:
                        startyear = year1
                        endyear = year2
                #for all the years more than the start year in the endyear range, print leapyear or nah
                for years in range((endyear+1)):
                        if years<startyear:
                                pass
                        else:
                                if is_leap_year(years):
                                        print years, "is a leap year"
                                else:
                                        print years, "is a normal year"

# finally, call main. Which makes the code work
main()
