import numpy as np

from common import MyWav


def MovingAverage(my_wav: MyWav, n) -> MyWav:
    samples = np.array([np.convolve(sample, np.ones(n), 'valid') / n for sample in my_wav.samples])
    nframes = len(samples[0])
    return MyWav(my_wav.nchannels, my_wav.sampwidth, my_wav.framerate, nframes, samples, my_wav.sample_type, my_wav.peak)
