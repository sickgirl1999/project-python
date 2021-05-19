
import numpy as np  # numerical python
import os
import cv2  # openCV - image processing

from numpy.random import seed

seed(1)

from tensorflow import set_random_seed
set_random_seed(2)

#import tensorflow

#tensorflow.random.set_seed(2)
# TO get dataet path
path1 = os.getcwd()  # Current Working Directory
path = os.path.join(path1, 'tinydb1')

import random
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt  # graph plotting

data = os.listdir(path)
kernel = np.ones((2, 1), np.uint8)
kernel1 = np.ones((1, 1), np.uint8)
out = np.zeros((119, 227, 227))
label = []

from keras.models import load_model

# creates a HDF5 file 'my_model.h5'


# returns a compiled model
# identical to the previous one

d = 0
k = 0
m = 0
for i in data:
    path1 = os.path.join(path, i)
    print(path1)
    class_data = os.listdir(path1)
    print(class_data)
    m = d
    d = d + 1

    da = [m for x in range(len(class_data))]
    label.extend(da)
    m = m + 1
    for j in class_data:
        ## PREPROCESSING
        # 1.To read an image to matrix. 0 means read as GrayScale
        imag = cv2.imread(os.path.join(path1, j), 0)

        # 2.To resize to a std size
        imag = cv2.resize(imag, (227, 227))
        ##        imag=imag.reshape(1,250,250,1)
        ##        imag = cv2.Canny(imag,30,20)

        # 3. Gaussian Edge Detection
        ou = cv2.adaptiveThreshold(imag, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 5)
        ##        ou = cv2.erode(ou, kernel1, iterations=1)
        ou = cv2.morphologyEx(ou, cv2.MORPH_OPEN, kernel)

        ou = ou.reshape(227, 227)
        cv2.imshow("leaf", ou)
        cv2.waitKey(1)
        ou = 255 - ou
        ou = np.multiply(imag, ou)
        cv2.imshow('leaf', ou)
        cv2.destroyAllWindows
        cv2.waitKey(1)
        out[k, :, :] = ou  # 3d matrix to store images

        k = k + 1
cv2.destroyAllWindows()

cv2.imshow('leaf1', out[20, :, :])
cv2.waitKey(1)
cv2.destroyAllWindows