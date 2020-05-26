import pandas as pd
import keras
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import one_hot


nome = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\nome_Data_Traces\18717010_events.csv', header=None)
oneme = pd.read_csv(r'C:\Users\Elijah\PycharmProjects\abfFiles\v2\1me_Data_Traces\19219008_events.csv', header=None)
Y = pd.read_csv(r'C:\Users\Elijah\Documents\real_labels_sample_7_2_19.csv', header = None)


X1= nome[0:10]

X2=oneme[0:10]

X = pd.concat([X1, X2], ignore_index=True)

x_train, x_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.25, shuffle= True)

# The known number of output classes.
num_classes = 3

# Input image dimensions
#input_shape = (4,)


# Convert class vectors to binary class matrices. This uses 1 hot encoding.
y_train_binary = keras.utils.to_categorical(y_train, num_classes)
y_test_binary = keras.utils.to_categorical(y_test, num_classes)

#########################################

# from numpy import array
# from numpy import argmax
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
#
# data = ['1me', 'nome']
# values = array(data)
#
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(values)
#
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
#
# print(onehot_encoded)
#############################################

x_train = x_train.reshape(15, 1000,1)
x_test = x_test.reshape(5, 1000,1)

from keras.models import Sequential
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv1D
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
from keras import backend as K

model = Sequential()
model.add(Conv1D(32, (3), input_shape=(1000,1), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='softmax'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

#model.summary()

batch_size = 16
epochs = 10
model.fit(x_train, y_train_binary,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test_binary))




