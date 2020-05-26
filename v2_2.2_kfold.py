global counter
counter = 0

import sklearn.model_selection as modelselection
from sklearn.model_selection import KFold
import keras.backend as K
from ImageModels.ResNet50 import ResNet50
from ImageModels.GetImages_v3 import loadImages
import pandas as pd
import numpy as np
from numpy import random
from random import sample
from sklearn.model_selection import train_test_split
from Label_Generation import genLabels
import keras
from keras.wrappers.scikit_learn import KerasClassifier

K.set_image_data_format('channels_last')
K.set_learning_phase(1)

# loading images of 1me class

#308 images
images_1me = loadImages(r"C:/Users/Elijah/Documents/NanoporeData/AllPlots/1me/", "1me_ImageData.csv")

# Placing images into a new array, at random
modeldata_1me = []
randIndices_1me = []

randIndices_1me = sample(range(0, 308), 218)

for i in range(0, len(randIndices_1me)):
    modeldata_1me.append(images_1me[randIndices_1me[i]])

# Ensuring that data is in a numpy array, for compatibility
modeldata_1me = np.asarray(modeldata_1me)

# print(randIndices_1me)
# print(len(randIndices_1me))
# print(modeldata_1me.shape)


# same randomizing process used for 1me, now used for nome
#222 nome plots total
images_nome = loadImages(r"C:/Users/Elijah/Documents/NanoporeData/AllPlots/nome/", "Nome_ImageData.csv")
modeldata_nome = []
randIndices_nome = []
randIndices_nome = sample(range(0, 222),218)

for i in range(0, len(randIndices_nome)):
    modeldata_nome.append(images_nome[randIndices_nome[i]])

modeldata_nome = np.asarray(modeldata_nome)

# print(randIndices_nome)
# print(len(randIndices_nome))
# print(modeldata_nome.shape)


# unifying both arrays of image data
X = np.concatenate((modeldata_nome, modeldata_1me))

#generating labels
genLabels(218,436)
Y = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\ImageModels\Dataset_Labels.csv', header = None)
Y = Y[0:436]
# print(Y)

# creating one-hot vectors for labels
Y = keras.utils.to_categorical(Y, 2)

# print("X shape")c
# print(X.shape)
#
# print("Y shape")
# print(Y.shape)


# using K-Fold Cross Validation, training on each fold
cvscores = []
count = []
kfold = KFold(n_splits=3, shuffle = True, random_state=1)
# x_train, x_test, y_train, y_test = train_test_split(X, np.asarray(Y), test_size=.25, shuffle= True, random_state=counter)
for train, test in kfold.split(X, Y):
    model = ResNet50(input_shape = (64, 64, 1), classes = 2)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X[train], Y[train], batch_size= 32, epochs= 3, verbose = 1, validation_data =(X[test], Y[test]))
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    cvscores.append(scores[1] * 100)
    count.append(1)
print((np.mean(cvscores), np.min(cvscores), np.max(cvscores), np.std(cvscores)))






