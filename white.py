#set path and initilaise variables
from PIL import Image
import os

path = 'E:\\yoda\\remove\\photos'

output_path = 'E:\\yoda\\remove\\output'

# contains the filenames 
names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

if not os.path.exists(output_path):
    os.makedirs(output_path)

for _file in names:
    image = Image.open(os.path.join(path, _file))
    image = image.convert('RGBA')
    # Transparency
    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)
    image.putdata(newImage)
    image.save(os.path.join(output_path, _file))