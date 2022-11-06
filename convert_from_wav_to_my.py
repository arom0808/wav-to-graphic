import numpy as np
import wave

from common import MyWav, types


def ConvertFromWavToMy(wav_filename: str) -> MyWav:
    wav = wave.open(wav_filename, mode='r')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav.getparams()
    raw_samples = np.frombuffer(wav.readframes(nframes), dtype=types[sampwidth])
    wav.close()
    samples = np.zeros((nchannels, nframes), dtype=types[sampwidth])
    peak = int(256 ** sampwidth)
    for n in range(nchannels):
        samples[n] = raw_samples[n::nchannels] - peak
    return MyWav(nchannels, sampwidth, framerate, nframes, samples, types[sampwidth], peak)
