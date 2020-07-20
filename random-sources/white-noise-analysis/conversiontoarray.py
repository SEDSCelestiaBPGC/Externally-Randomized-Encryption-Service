import numpy as np
import pydub
from pydub import AudioSegment



class Arrayconversion:

    def mp3toarray(self,src):
        sound = np.asarray(pydub.AudioSegment.from_mp3(src).get_array_of_samples(),
            dtype = np.int64)
        return sound





















