import os

# folder path ro remove files from
root = 'E:\\yoda\\Train\\Outdoor'

#folder path to cross check with and use as a reference to delete files from 'root'
dest = 'C:\\Users\\User\\Downloads\\Outdoor'

#variables containing the filenames in each folder as an array

rootfiles = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
destfiles = [f for f in os.listdir(dest) if os.path.isfile(os.path.join(dest, f))]


for _file in destfiles:
# comment out if file extension is same for both folders
    name, extension = os.path.splitext(_file)
    name = name+'.png'
# code to remove files from root
    os.remove(os.path.join(root, name))
    