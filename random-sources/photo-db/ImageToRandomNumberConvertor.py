import numpy as np
import cv2
import random
import re
import os

'''
PR #2:
    step1 was done using the resize function of opencv
    step2 was done by splitting each row of the resultant N X N X 3 matrix into parts of lenght W X 3 each and then were stacked on top of the other to obtain a 
    (N/W) X (N/W) X (W * W) X 3 matrices
    step3 was done by finding the RBG channel averages for each entry (each of ((W*W) X 3) matrices) in the resultant matrix using python broadcasting. 
    The public member of the below class namely, get_avg_colours_img(imageFile, N, W) takes three arguments 
    imageFile: filepath
    N: resizing parameter
    W: spliting parameter
    It is always expected that N >= W
    This function returns final answer as a list of averages of the channel values for each of the (W*W) X 3 matrices
    The resultant answer will be of form ((N/W) * (N/W)) X 3
PR #9:
    Function get_binary_stream(self, path, N, W, threshold, numOfImages) was created for this. Its parameters are:
    path: path to images
    N: same as the N in get_avg_colours_img(imageFile, N, W)
    W: same as the W in get_avg_colours_img(imageFile, N, W)
    threshold: used to append either a 1 or 0 to final binary string.
    numOfImages: number of Images you want to use from the path directory (set to -1 if you want all).
    
    This function first calls the get_list_of_arrays_from_images(self, path, N, W, numOfImages) to get an array of size
    X x ((N/W) * (N/W)) X 3 (for X images) and stores it in x.
    Then it calls get_arrays_randomly(x) to select one of 1 x 3 matrices from each of the X arrays of dimension ((N/W) * (N/W)) X 3 and stores it in a numpy array.
    Then a call is made to convert_to_binary(getArraysForConversion, threshold), which gets the sum of each entry in the array and converts it to binary based on a threshold.
     (A preferable value for threshold is around 0.075 from what I tested)
    
    The final binary numpy array is stored in final and returned.
'''

class ImageToRandomNumberConvertor:
    nums = re.compile(r'(\d+)')
    def __key(self, value):
        parts = self.nums.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts
    
    def __sum(self, list):
        sum = 0

        for i in list:
            sum += i

        return sum

    def __averageOfColorsOfImages(self, imgs, W):
        averages = []

        for entry in imgs:
            for img in entry:
                av = self.__sum(img) / (W * W)
                averages.append(av)

        averages = np.array(averages)

        return averages

    def __appendToBuffer(self, buffer, i):
        newBuffer = []
        count = 0
        if len(buffer) == 0: return i

        for buf in buffer:
            buf = np.vstack((buf, i[count]))
            newBuffer.append(buf)
            count += 1

        return newBuffer

    def __horizontal_split(self, i, W):
        buffer = []
        add = []
        counter = 0

        for iterator in i:
            add.append(iterator)
            counter += 1
            if(counter % W == 0):
                buffer.append(add)
                add = []

        return buffer


    def __split(self, img, N, W):
        new_imgs = []
        count  = 0
        buffer = []

        for i in img:
            if N%W != 0:
                i = i[:-(N%W)]
            i = self.__horizontal_split(i, W)
            buffer = self.__appendToBuffer(buffer, i)
            count += 1
            if(count % W == 0):
                new_imgs.append(buffer)
                buffer = []

        new_imgs = np.array(new_imgs)
        return new_imgs

    def __get_avg_colours_img(self, imageFile, N, W):
        if( N < W ): return 0
        
        img = cv2.imread(imageFile)
        
        img = cv2.resize(img, (N, N)) # step 1
        imgs = self.__split(img, N, W) # step 2
        values = self.__averageOfColorsOfImages(imgs, W) # step 3

        return values
        
    
    def __get_list_of_arrays_from_images(self, path, N, W, numOfImages):
        x = []
        counter = 0
        
        for i in sorted(os.listdir(path),key=self.__key):
            imgFile = path + '\\' + i
            buf = self.__get_avg_colours_img(imgFile, N, W)
            x.append(buf)
            counter += 1
            if(counter == numOfImages): break
        
        x = np.array(x)
        
        return x
    
    def __get_arrays_randomly(self, x):
        getArraysForConversion = []
        
        for i in x:
            n = random.randint(0, len(i) - 1)
            getArraysForConversion.append(i[n])
        
        getArraysForConversion = np.array(getArraysForConversion)
        
        return getArraysForConversion
    
    def __convert_to_binary(self, getArraysForConversion, threshold):
        final = []
        
        for i in getArraysForConversion:
            val = sum(i)
            
            if(val >= threshold): final.append(1)
            else: final.append(0)
            
        final = np.array(final)
        
        return final
    
    def get_binary_stream(self, path, N, W, threshold, numOfImages):
        x = self.__get_list_of_arrays_from_images(path, N, W, numOfImages)
        getArraysForConversion = self.__get_arrays_randomly(x)
        final = self.__convert_to_binary(getArraysForConversion, threshold)

        return final
  
