import numpy as np


def AudioFramesPerVideoFrames(fps: int, framerate: int) -> np.ndarray:
    audio_frames_per_video_frames = np.full(fps, framerate // fps)
    if framerate % fps != 0:
        step = fps // (framerate % fps)
        for i in range(0, step * (framerate % fps), step):
            audio_frames_per_video_frames[i] += 1
    return audio_frames_per_video_frames
