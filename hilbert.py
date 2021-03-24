import scipy.signal as sign
import numpy as np

def hilbert(data):
    analytical_signal = sign.hilbert(data)
    amplitude_envelope = np.abs(analytical_signal)
    return amplitude_envelope
