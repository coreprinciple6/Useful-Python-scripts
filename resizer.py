
import os
import pandas as pd
from PIL import Image
import numpy as np
from numpy import load
from numpy import save


# path to images
path = 'E:\\yoda\\mistake'


#path were resized img will be saved (final)
output =  'E:/yoda/final'


#loop for resizing mfcc images

imgfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for _file in imgfiles:
    img = Image.open((os.path.join(path, _file)))
    new_image = img.resize((224, 224))
    name, extension = os.path.splitext(_file)
    new_image.save((os.path.join(output,name))+'.png')


