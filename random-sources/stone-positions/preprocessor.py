# -*- coding: utf-8 -*-
"""rice_and_stones_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r0FBgDJazSghY2gQtLkZKKmFKTtXp3a8
"""

import cv2

class rice_stones_prep:
    def __init__(self, img_path):
        #img_path should be of format '/path/to/image.file'
        self.img_path = img_path
        self.img = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)
    
    def __thresh(self, img, thr_val):
        ret, thresh_img = cv2.threshold(img, thr_val, 255, cv2.THRESH_BINARY)
        return thresh_img
    
    def __resize(self, img, dim):
        resized_img = cv2.resize(img, (dim, dim))
        return resized_img
    
    def __blur(self, img):
        blur_img = cv2.medianBlur(img,5)
        return blur_img
    
    def img_prep(self, N, T):
        img = self.__resize(self.img, N)                                   #resizing img
        img = self.__thresh(img, T)                                  #threshold
        final_img = self.__blur(img)                                    #blur
        return final_img
    
    #only for test runs
    def test_py(self, img, windowName):                                                  #use in case of .py implementations
        cv2.namedWindow(windowName)
        cv2.imshow(windowName, img)
        cv2.waitKey()
       
    def test_ipynb(self, img):                                               #because cv2.imshow doesn't work on jupyter notebooks
        plt.figure(figsize=(7,7))
        plt.imshow(img)
        plt.axis('off')
        plt.show()