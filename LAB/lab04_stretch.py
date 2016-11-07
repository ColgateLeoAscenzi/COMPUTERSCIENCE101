#Leo Ascenzi
import image
img = image.load_from_file('crayons.png')
w = img.width()
h = img.height()

print "The original dimensions of the image are: %s x %s" % (w, h)
w1 = int(raw_input("Width?: "))
h1 = int(raw_input("Height?: "))
imgs = image.new_image(w1, h1)
multx = float(w1)/w
multy = float(h1)/h

for y in range(h1):
    for x in range(w1):
        r, g, b = img.get_rgb(int(x/multx),int(y/multy))
        imgs.set_rgb(x,y,r,g,b)


image.display_images(imgs)

