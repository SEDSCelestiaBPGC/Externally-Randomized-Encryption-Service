import numpy as np
import cv2

'''
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
'''

class ImageToRandomNumberConvertor:
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
            i = i[:-(N%W)]
            i = self.__horizontal_split(i, W)
            buffer = self.__appendToBuffer(buffer, i)
            count += 1
            if(count % W == 0):
                new_imgs.append(buffer)
                buffer = []

        new_imgs = np.array(new_imgs)
        return new_imgs

    def get_avg_colours_img(self, imageFile, N, W):
        if( N < W ): return 0
        img = cv2.imread(imageFile)
        img = cv2.resize(img, (N, N)) # step 1
        imgs = self.__split(img, N, W) # step 2
        values = self.__averageOfColorsOfImages(imgs, W) # step 3

        return values