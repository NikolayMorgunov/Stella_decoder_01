from scipy.io.wavfile import read
import numpy as np
import scipy.signal as sign
import matplotlib.pyplot as plt
from hilbert import *
from draw_a_pic import *

file = 'signal.WAV'

samplerate, data = read(file)
data_crop = data[220 * samplerate: 221 * samplerate]

fig = plt.figure()

# plt.plot(data_crop)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.title("Signal")
new_sample = 2080


data_am_crop = hilbert(data_crop)
data_am = hilbert(data)

new_fs = 2080
number_of_samples = round(len(data_am) * float(new_fs)/samplerate)
data_ready = sign.resample(data_am, number_of_samples)
samplerate = new_fs

# plt.plot(data_am)

# resample = 4
# data_am = data_am[::resample]
# samplerate = samplerate // resample

# data_ready = []
# for i in range(0, len(data_am), new_sample):
#     data_ready.append(data_am[i])
# samplerate = new_sample



draw(samplerate, data_ready)
