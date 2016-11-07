#Leo Ascenzi
import image
img = image.load_from_file('secret_message.png')
ns = ""
w = img.width()
h = img.height()
for y in range(h):
    for x in range(w):
        r, g, b = img.get_rgb(x, y)
        if r == 13:
            ns = ns + chr((g+b))
print ns


        
