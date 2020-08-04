import cv2
import numpy as np

class stone_detector:
    def __init__(self, prep_img):
      self.img = prep_img
    
    def blob_detector(self, print_bool = True):
      detector = cv2.SimpleBlobDetector_create()
      keypoints = detector.detect(self.img)
      img_with_keypoints = cv2.drawKeypoints(self.img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
      if(print_bool == True):
          cv2.namedWindow("stones")
          cv2.imshow("stones", img_with_keypoints)
          cv2.waitKey()
      return img_with_keypoints, keypoints

    def coordinates(self, print_bool = False):
      im_with_keypoints, keypoints = self.blob_detector(print_bool)
      pts = np.asarray([[p.pt[0], p.pt[1]] for p in keypoints])
      return pts




  


