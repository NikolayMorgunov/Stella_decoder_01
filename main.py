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

max_d = max(data_am)
data_am = [i * 255 // max_d for i in data_am]
data_am, matrix = find_synchro(samplerate, data_am)

draw(samplerate, data_am)
