import sys
import os
from PIL import Image

#Grab the first and second argument
input_folder = sys.argv[1]
output_folder = sys.argv[2]

print(input_folder,output_folder)

#check whether \new exist or not if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through given folder and convert it to png and save it too
for file in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{file}')
    clean = os.path.splitext(file) 
    (name,extension) = clean
    #basically it gives tuple 
    """
    ('astro', '.jpg')
    ('pikachu', '.jpg')
    """
    print(name)
    img.save(f'{output_folder}{name}.png','png')
    """
    when we doing normally it not saving in png infact it is in jpg.png #wierdo
    so we have to remove the jpg then add png format
    """
    print("all done!!")