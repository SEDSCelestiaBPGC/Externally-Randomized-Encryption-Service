
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
from preprocessor import *
from detector import *
from randomize import *


N = 360                                                     #reqd. image sq. dimension
T = 90
img_path1 = "C:\\Users\\Aeishna\\Downloads\\marbles.jpg"
img_path2 = "C:\\Users\\Aeishna\\Downloads\\IMG_20200721_121939.jpg"
img_path3 = "C:\\Users\\Aeishna\\Downloads\\marbles2.jpg"
preprocessed = rice_stones_prep(img_path1)
final_img = preprocessed.img_prep(N, T)

detected = stone_detector(final_img)
pts = detected.coordinates()
print(pts)
randomized = randomize(pts)
random_sequence = randomized.randomBinPoints()
print(len(random_sequence))



# To compare detection of points

# im_with_keypoints, keypoints = detected.blob_detector(False)
# f, (ax1, ax2) = plt.subplots(1, 2)
# ax1.imshow(final_img)

# cols_2 = pts[:,0]
# rows_2 = pts[:,1]
# ax2.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
# ax2.scatter(cols_2, rows_2)

# plt.show()

# detector = stone_detector(final_img)
# detector.blob_detector(True)