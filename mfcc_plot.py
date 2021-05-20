import os
from scipy.io import wavfile
from sklearn import preprocessing
from sklearn import preprocessing
import python_speech_features as mfcc

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#set path and initilaise variables

# path to audiofiles
path = 'E:\\yoda\\Terminal Dset\\Train\\Outdoor'

# path where high res img will be saved
root =  'E:\\redemption'

# contains the audio filenames 
filename = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for _file in filename:
	sampling_rate, audio_signal =wavfile.read((os.path.join(path, _file)))
	feature = mfcc.mfcc(audio_signal,96000  , 0.01, 0.001,numcep=20, nfilt=20, nfft = 1000)   
	feature = preprocessing.scale(feature)

	fig = plt.Figure()
	canvas = FigureCanvas(fig)
	ax = fig.add_subplot(111)
	librosa.display.specshow(librosa.amplitude_to_db(feature, ref=np.max), ax=ax)
	name, extension = os.path.splitext(_file)
	fig.savefig((os.path.join(root, name))+ '.png')
