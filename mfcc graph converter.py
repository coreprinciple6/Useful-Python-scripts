
#import libraries
import os
import pandas as pd
from PIL import Image
import numpy as np
from numpy import load
from numpy import save
from sklearn import preprocessing
import python_speech_features as mfcc
from scipy.io import wavfile


#set path and initilaise variables

# path to audiofiles
path = 'E:\\light\\audio'

# path where high res img will be saved
root =  'E:\\light\\temp'

#path were resized img will be saved (final)
output =  'E:/yoda/final'


# contains the audio filenames 
filename = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]



import matplotlib.pyplot as plt

# loop to produce mfcc graphs
for _file in filename:
    sampling_rate, audio_signal =wavfile.read((os.path.join(path, _file)))
    mfcc_feature = mfcc.mfcc(audio_signal,sampling_rate, 0.01, 0.001,numcep=20,nfilt=30,nfft = 1200, appendEnergy = True)    
    mfcc_feature = preprocessing.scale(mfcc_feature)

    #plot mfcc as a graph
    plt.plot(mfcc_feature)
    plt.axis('off')
    name, extension = os.path.splitext(_file)
    #save graph
    plt.savefig((os.path.join(root, name))+ '.png' ,  bbox_inches='tight', dpi = 200 )


#loop for resizing mfcc images to (224x224)
imgfiles = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]

for _file in imgfiles:
    img = Image.open((os.path.join(root, _file)))
    new_image = img.resize((224, 224))
    name, extension = os.path.splitext(_file)
    new_image.save((os.path.join(output,name))+'.png')


