import sys
import os
from PIL import Image

infolder , outfolder = sys.argv[1:3]

# if os.path.isdir(outfolder) == False:    #one way to check if folder exist
#     os.mkdir(outfolder)

if not os.path.exists(outfolder):
    os.mkdir(outfolder)


for file in os.listdir(infolder):
    path = outfolder + '/' + file.split('.')[0] + '.png'
    with Image.open(infolder + '/' + file) as im:
        im.save(path)
        print("Done")