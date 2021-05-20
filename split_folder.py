import os, os.path, shutil


# source path 
path = './Outdoor'

# destination path that will hold sub directories
folder_path = './cat'

images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

count = 1   # for counting files
dir = 1     # for naming directories

# variable to hold the number of files each subdirectory will have plus 1
x = 200 +1

for img in images:

    if(count%x==0):
        count = 1
        dir = dir+1

    folder = os.path.join(folder_path, 'in'+str(dir))
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.move(os.path.join(path, img), folder)
    count = count+1
