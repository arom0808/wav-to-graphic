import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import *
from moviepy.video.io.bindings import mplfig_to_npimage

from common import MyWav


def make_frame(t, my_wav: MyWav, basic_graphic_data: np.ndarray, fps: int, axs, x: np.ndarray, fig):
    frame_id = round(t * fps)
    for n in range(my_wav.nchannels):
        axs[n].clear()
        axs[n].set_xlim(0, 1)
        axs[n].set_ylim(0, 0.15)
        axs[n].fill_between(x, basic_graphic_data[n][frame_id])
    return mplfig_to_npimage(fig)


def ConvertGraphicDataToVideo(audio_file: str, out_video_file: str, my_wav: MyWav, basic_graphic_data: np.ndarray,
                              fps: int):
    duration = my_wav.nframes // my_wav.framerate
    x = np.linspace(0, 1, 2)

    fig, axs = plt.subplots(ncols=my_wav.nchannels, sharey="all")

    make_frame_shell = lambda t: make_frame(t, my_wav, basic_graphic_data, fps, axs, x, fig)

    animation = VideoClip(make_frame_shell, duration=duration).set_audio(AudioFileClip(audio_file))
    # animation.preview()
    animation.write_videofile(out_video_file, fps=fps)
