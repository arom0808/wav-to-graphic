from convert_from_my_to_basic_graphic_data import ConvertFromMyToBasicGraphicData
from convert_from_wav_to_my import ConvertFromWavToMy
from convert_graphic_data_to_video import ConvertGraphicDataToVideo
from moving_average import MovingAverage

fps = 60
my_wav = ConvertFromWavToMy('chinese-song-LAY.wav')
my_wav = MovingAverage(my_wav, int(my_wav.framerate / 20))
basic_graphic_data = ConvertFromMyToBasicGraphicData(my_wav, fps)
ConvertGraphicDataToVideo('chinese-song-LAY.wav', 'chinese-song-LAY.mp4', my_wav, basic_graphic_data, fps)
