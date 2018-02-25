from PIL import Image
import random
import os

for i in range(10):
    dir = "./%d" % i
    if not os.path.exists(dir):
        os.makedirs(dir)

name = "016586.jpeg"
value = name.split(".")[0]
im = Image.open(name)
x = 5
y = 0
w = 13
h = 20
for i in range(6):
    x += w if i > 0 else 0 
    region = im.crop((x, y, x + w, y + h))
    name = random.randint(1, 9999)
    region.save("./%s/%d.jpeg" % (value[i], name))