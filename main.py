from scipy.io.wavfile import read
import numpy as np
import scipy.signal as sign
from hilbert import *
from draw_a_pic import *
from synchro import *

file = 'signal.WAV'

samplerate, data = read(file)

data_am = data.copy()
# data_am_crop = hilbert(data_crop)
data_am = hilbert(data_am)

# plt.plot(data_am)

# resample = 4
# data_am = data_am[::resample]
# samplerate = samplerate // resample

# data_ready = []
# for i in range(0, len(data_am), new_sample):
#     data_ready.append(data_am[i])
# samplerate = new_sample


max_d = max(data_am)
data_am = [i * 255 // max_d for i in data_am]
data_am = find_synchro(samplerate, data_am)

draw(samplerate, data_am)
