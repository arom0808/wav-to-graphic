import math
from collections import namedtuple
import numpy as np

from constants import EPSILON

types = {
    1: np.uint8,
    2: np.uint16,
    4: np.uint32
}

MyWav = namedtuple('MyWav',
                   ['nchannels', 'sampwidth', 'framerate', 'nframes', 'samples', 'sample_type', 'peak'])


def ConvertFromAmplitudeToVolume(x: int, peak: int) -> float:
    volume = math.pow(EPSILON, 1 - (abs(x) / float(peak)))
    return volume if volume > EPSILON else 0
