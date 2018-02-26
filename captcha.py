from PIL import Image
import random
import os

imageDir = "./digit_images"
if not os.path.exists(imageDir):
    os.makedirs(imageDir)

for i in range(10):
    dir = "./%s/%d" % (imageDir, i)
    if not os.path.exists(dir):
        os.makedirs(dir)

dataDir = "./captcha/"
y = 0
w = 13
h = 20

for name in os.listdir(dataDir):
    x = 5
    value = name.split(".")[0]
    im = Image.open(dataDir + name)
    for i in range(6):
        x += w if i > 0 else 0 
        region = im.crop((x, y, x + w, y + h))
        segmentName = random.randint(1, 9999)
        region.save("./%s/%s/%d.jpeg" % (imageDir, value[i], segmentName))