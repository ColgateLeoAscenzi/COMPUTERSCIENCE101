#Leo Ascenzi
import image
spring = image.load_from_file('spring.png')
winter = image.load_from_file('winter.png')
img = image.new_image(728, 546)

h = img.height()
w = img.width()
for y in range(h):
    for x in range(w):
        if x%2 == 0:
            r, g, b = winter.get_rgb(x, y)
            img.set_rgb(x,y,r,g,b)
            r, g, b = spring.get_rgb(x, y)
            img.set_rgb(x,y,r,g,b)

image.display_images(img)
