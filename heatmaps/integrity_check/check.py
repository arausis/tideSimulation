from PIL import Image
import PIL
import numpy as np
import os
  
# Import an image from directory: 
current_directory = os.path.dirname(os.path.abspath(__file__))

DIR = current_directory + "/test.png"
input_image = Image.open(DIR) 

# Extracting pixel map: 
pixel_map = input_image.load()
  
width, height = input_image.size 
print(width)
print(height)

def transform(r, g, b):
    return r,g,b
  
for i in range(width): 
    for j in range(height): 
        r, g, b = input_image.getpixel((i, j)) 
        if( j == 0):
            print(r)
            print(g)
            print(b)
            print()
