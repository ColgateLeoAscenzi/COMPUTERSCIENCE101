# ----------------------------------------------------------
# HW 4
# ----------------------------------------------------------
# Please answer these questions after having completed the 
# entire assignment.
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent in total:  4
# Collaborators (if any): No one as usual :( 
# Feedback: What was the hardest part of this assignment?
#   <Making some of the logic for the posterize
#   took a bit of tweaking. Spelling posterize
#   with an E and not a U. Like posturize was
#   also very hard and caused frustration>
# Feedback: Any suggestions for improving the assignment?	
#   <Overall this was fun, but I would say make posterize
#   the challenge problem. The keying-out problem could've
#   been the 2nd or 3rd problem in this assignment. It took
#   me about 1/10th of the time as 4, 5 and 6 individually.
# ----------------------------------------------------------


import image

## -------------------------------
## EXAMPLE FUNCTION: RED FILTER
## -------------------------------
## here's an example of a function definition
## the function call appears inside the main()
## function body below
##def red_filter(img):
##    """
##    (Image object) -> Image object
##    Returns a copy of img where the blue and green have been filtered out
##    and only red remains.
##    """
##    red_only_img = image.copy_image(img)
##    # loop over every (x,y) pair
##    for x in range(img.width()):
##        for y in range(img.height()):
##            # filter out green and blue
##            red_only_img.set_green(x, y, 0)
##            red_only_img.set_blue(x, y, 0)
##    return red_only_img  # return img object

# -------------------------------
# BEGIN GRADED TRANSFORMATIONS
# -------------------------------
# define your functions for graded transformations here
# - each function should be similar to red_filter in that it 
# takes an image object in and returns an image object
# - look at how red_filter is call in the main program below
# - be sure to include docstrings!

#1 - Cycles Colors
def color_cycle(img):
    '''(Image object) -> Image object
    Returns a copy of img where the red value has been
    moved to the blue value, the green to the red and
    the blue to the green
    '''
    img_cycled = image.copy_image(img)
    #loop over every(x,y) pair
    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)
            #sets the new colors
            img_cycled.set_red(x,y,g)
            img_cycled.set_green(x,y,b)
            img_cycled.set_blue(x,y,r)
    return img_cycled

#2 - Makes a grayscale image
def grayscale(img):
    '''(Image object) -> Image object
    Returns a copy of img where the rgb values
    have been averaged and reassigned, making a
    happy grey image
    '''
    img_grayer = image.copy_image(img)
    #loop over every (x,y) pair
    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)
            avg_pix = int(float(r+b+g)/3)
            img_grayer.set_rgb(x,y,avg_pix,avg_pix,avg_pix)

    return img_grayer

#3 - Makes the negative of an image
def negative(img):
    '''(Image object) -> Image object
    Returns a copy of img where the the rgb values
    are the opposite of what they normally are,
    meaning they're negative
    '''
    img_negative = image.copy_image(img)
    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)

            #Makes pixels negative
            r_neg = (r-255)
            if r_neg<0:
                r_neg = r_neg*-1
                
            g_neg = (g-255)
            if g_neg<0:
                g_neg = g_neg*-1
                
            b_neg = (b-255)
            if b_neg<0:
                b_neg = b_neg*-1

            #sets the new pixels
            img_negative.set_rgb(x,y,r_neg,g_neg,b_neg)

    return img_negative

#4 - Allows the user to change brightness
def brightness(img):
    '''(Image object) -> Image object
    Returns a copy of img where the the brightness
    is increased or decreased based on the users command
    '''
    br_value = int(raw_input("Please enter a number to adjust the brightness to: "))

    img_brightness = image.copy_image(img)

    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)

            #Generates new rgb values and doesn't let them exceed 255 or go below 0
            new_r = r + br_value
            if new_r>255:
                new_r = 255
            elif new_r<0:
                new_r = 0
            else:
                new_r = new_r

            new_g = g + br_value
            if new_g>255:
                new_g = 255
            elif new_g<0:
                new_g = 0
            else:
                new_g = new_g
                
            new_b = b + br_value
            if new_b>255:
                new_b = 255
            elif new_b<0:
                new_b = 0
            else:
                new_b = new_b
            
            img_brightness.set_rgb(x,y,new_r,new_g,new_b)
    return img_brightness    
#5 - Increases the contrast
def increase_contrast(img):
    '''(Image object) -> Image object
    Increases the contrast of img
    '''
    img_contrast = image.copy_image(img)

    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)
            #Sets the new rgb values
            new_r = 0
            new_g = 0
            new_b = 0

            #Checks whether or not to increase contrast, and doesn't allow too big or small values
            if r == 128:
                new_r = r
            elif r>128:
                new_r = r+(2*(r-128))
                if new_r>255:
                    new_r = 255
            else:
                new_r = r-(2*(128-r))
                if new_r<0:
                    new_r = 0

            if g == 128:
                new_g = g
            elif g>128:
                new_g = g+(2*(g-128))
                if new_g>255:
                    new_g = 255
            else:
                new_g = g-(2*(128-g))
                if new_g<0:
                    new_g = 0

            if b == 128:
                new_b = b
            elif b>128:
                new_b = b+(2*(b-128))
                if new_b>255:
                    new_b = 255
            else:
                new_b = b-(2*(128-b))
                if new_b<0:
                    new_b = 0

            #Sets the real new rgb values  
            img_contrast.set_rgb(x,y,new_r,new_g,new_b)


    return img_contrast

#6 - Posterizes the image GRADE THIS ONE :D wow colon d looks bad in IDLE
def posterize(img):
    '''(Image object) -> Image object
    Posterizes the img by reducing the
    amount of colors
    '''
    img_posterize = image.copy_image(img)

    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)
            new_r = r
            new_g = g
            new_b = b

            #Sets the new variables
            if r%32 == 0:
                new_r = r
            elif new_r%32 != 0:
                new_r = r-(r%32)

            if g%32 == 0:
                new_g = g
            elif new_g%32 != 0:
                new_g = g-(g%32)

            if b%32 == 0:
                new_b = b
            elif new_b%32 != 0:
                new_b = b-(b%32)

            

            #Sets each pixel
            img_posterize.set_rgb(x,y,new_r,new_g,new_b)

    return img_posterize

#7 - makes an image more political
def obamafy(img):
    '''(Image object) -> Image object
    Obamafys image by assigning a specific colour
    per grayscale value
    '''
    img_obamified = image.copy_image(img)
    #loop over every (x,y) pair
    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgb and sets it to r, g and b
            r,g,b = img.get_rgb(x,y)
            gray_value = int(float(r+b+g)/3)
            #yellow
            if gray_value>182:
                img_obamified.set_rgb(x,y, 252, 227, 166)
            #light blue
            elif 121<gray_value<182:
                img_obamified.set_rgb(x,y, 112, 150, 158)
            #red
            elif 60<gray_value<121:
                img_obamified.set_rgb(x,y, 217, 26, 33)
            #dark blue
            else:
                img_obamified.set_rgb(x,y, 0, 51, 76)
                
    return img_obamified

#"Challenge"
def key_out_red(img, img2):
    '''(Image object) + (Image object) -> Image object
    Checks to see what pixels in the img are red, and
    replaces them with pixels from another image
    '''
    img_red = image.copy_image(img)
    #loop over every (x,y) pair
    for x in range(img.width()):
        for y in range(img.height()):
            #gets the rgbs for each picture at the x and y of the original
            r,g,b = img.get_rgb(x,y)
            r1,g1,b1 = img2.get_rgb(x,y)
            #I found through playing with an online tool that things that are red
            #generally have an r value which is greater than the other two combined
            #So this checks if it's true
            if r>b+g:
                img_red.set_rgb(x,y,r1,g1,b1)
                
    return img_red
    

                        
#--------------------------------
# END GRADED TRANSFORMATIONS
#--------------------------------

# Remaining transformations may be placed in functions or in main()

def main():
    """
    () -> NoneType
    Main Program that load image(s) from file(s) and performs transformations!
    """

    #Loads the original image
    original_img = image.load_from_file('crayons.png')
    obamanation = image.load_from_file('obama.png')
    stopschild = image.load_from_file('stop_sign.png')
    blaetter = image.load_from_file('leaves.png')

    #Assign a bunch of variables and transforms more than Optimus Prime
    color_cycled = color_cycle(original_img)
    grayscaled = grayscale(original_img)
    negated = negative(original_img)
    brightered = brightness(original_img)
    contrasted = increase_contrast(original_img)
    posterized = posterize(original_img)
    obamafied = obamafy(obamanation)
    redded = key_out_red(stopschild, blaetter)

    #displays all images
    image.display_images(color_cycled, grayscaled, negated, brightered, contrasted, posterized)
    image.display_images(obamafied, redded)

main()
