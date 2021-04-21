from scipy.io.wavfile import read
import numpy as np
import scipy.signal as sign
from hilbert import *
from draw_a_pic import *
from synchro import *

file = 'signal.WAV'

samplerate, data = read(file)

data_am = data.copy()
data_am = hilbert(data_am)

max_d = max(data_am[314*5512:653*5512])
min_d = min(data_am[314*5512:653*5512])
print(max_d, min_d)
data_am = [((i - min_d) * 255) // (max_d - min_d) for i in data_am]
data_am, matrix = find_synchro(samplerate, data_am)

draw(samplerate, data_am)
