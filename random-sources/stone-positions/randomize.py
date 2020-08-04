import cv2
import numpy as np

class randomize:
    def __init__(self, pts):
        self.pts = pts
    
    def __sortArray(self, columnIndex):
        sortedArr = self.pts[self.pts[:,columnIndex].argsort()]
        return sortedArr
    
    def randomPoints(self):
        # sortArray = self.__sortArray(columnIndex)
        cy = np.asarray([p[1] for p in self.__sortArray(0)])
        cx = np.asarray([p[0] for p in self.__sortArray(1)])
        random_sequence = np.concatenate ([cx,cy], axis=None)
        return random_sequence
