from os import listdir
import keras_preprocessing.image as kerasimg
from tensorflow import image as tensorimg
import cv2
import numpy as np
##image retrieval and resizing


def loadImages(path, csvName):
    imagesList = listdir(path)

    data = []

    for image in imagesList:
        img = kerasimg.load_img(path + image, grayscale=True, color_mode='rgb', target_size=(64, 64))
        # img = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
        # img = cv2.resize(img, (64, 64))
        img = kerasimg.img_to_array(img)
        data.append(img)

    return data