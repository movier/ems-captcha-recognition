from PIL import Image
import random

name = "unknow.jpg"

y = 0
w = 13
h = 20

x = 5

im = Image.open(name)
for i in range(6):
    x += w if i > 0 else 0 
    region = im.crop((x, y, x + w, y + h))
    resize = region.resize((128, 197), Image.BILINEAR)
    segmentName = random.randint(1, 9999)
    resize.save("%d.jpeg" % segmentName)