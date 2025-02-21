#35, 22.5
#40.8, 22.5
#40.8, 28.5
#35, 28.5
from PIL import Image
import PIL
import numpy as np
import os
  
# Import an image from directory: 
current_directory = os.path.dirname(os.path.abspath(__file__))
DIR = current_directory + "/eflow.png"
landDIR = current_directory + "/land.png"
input_image = Image.open(DIR) 
imland = Image.open(landDIR)

# Extracting pixel map: 
pixel_map = input_image.load()
land = imland.load()
im = PIL.Image.new(mode="RGB", size=( 350, 380))
newpixel_map = im.load()
  
# Extracting the width and height  
# of the image: 
width, height = input_image.size 
print(width)
print(height)

def transform(r, g, b):
    return r,g,b
  
# taking half of the width: 
for i in range(width): 
    for j in range(height): 
        if (i > 350) and (i <= 700) and (j > 70) and (j <= 450):
            r, g, b = input_image.getpixel((i, j)) 
            r2, g2, b2 = imland.getpixel((i, j))
            if (r2 + g2 + b2 < 350):
                newpixel_map[i-351, j-71] = (255, 0, 0) 
            else:
                r,g,b = transform(r,g,b)
                newpixel_map[i-351, j-71] = (r,g,b)

im.save("eflowcropped.png", format="png") 
  
# use input_image.show() to see the image on the 
# output screen. 
