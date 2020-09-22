# audio editor

import pydub
import numpy as np
import simpleaudio

def read(f, normalized=True):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y

sr, x = read(r"D:\Engineering_1\venv\sound_music\top.mp3")

print(x.shape)
print(x[1000:1020])

#x = np.repeat(x,repeats=2,axis=0)
x = np.delete(x, list(range(0, x.shape[0], 7)), axis=0)
#x = np.array([i-0.05 for i in x])



def write(f, sr, x, normalized=True):
    """numpy array to MP3"""
    channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
    if normalized:  # normalized array - each item should be a float in [-1, 1)
        y = np.int16(x * 2 ** 15)
    else:
        y = np.int16(x)
    song = pydub.AudioSegment(y.tobytes(), frame_rate=sr, sample_width=2, channels=channels)
    song.export(f, format="mp3", bitrate="320k")

write("top_out_fast.mp3",sr,x)

