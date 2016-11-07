#Leo Ascenzi
import image
img = image.load_from_file('landmark_puzzle.png')

h = img.height()
w = img.width()
for x in range(w):
    for y in range(h):
        r, g, b = img.get_rgb(x,y)
        img.set_rgb(x, y,0,g*25,0)

image.display_images(img)
