import numpy as np

from audio_frames_per_video_frames import AudioFramesPerVideoFrames
from common import ConvertFromAmplitudeToVolume
from convert_from_wav_to_my import MyWav


def ConvertFromMyToBasicGraphicData(my_wav: MyWav, fps: int) -> np.ndarray:
    audio_frames_per_video_frames = AudioFramesPerVideoFrames(fps, my_wav.framerate)
    video_frames_count = my_wav.nframes // my_wav.framerate * fps
    used_audio_frames_count = my_wav.nframes // my_wav.framerate * my_wav.framerate
    if used_audio_frames_count < my_wav.nframes:
        for afpvf in audio_frames_per_video_frames:
            video_frames_count += 1
            used_audio_frames_count += afpvf
            if used_audio_frames_count >= my_wav.nframes:
                break
    basic_graphic_data = np.zeros((my_wav.nchannels, video_frames_count), dtype=np.float64)
    used_audio_frames_count = 0
    for i in range(video_frames_count):
        frames_to_read_count = min(audio_frames_per_video_frames[i % fps], my_wav.nframes - used_audio_frames_count)
        for n in range(my_wav.nchannels):
            avg = np.average(my_wav.samples[n][used_audio_frames_count:used_audio_frames_count + frames_to_read_count])
            basic_graphic_data[n][i] = ConvertFromAmplitudeToVolume(avg, my_wav.peak)
        used_audio_frames_count += frames_to_read_count
    return basic_graphic_data
