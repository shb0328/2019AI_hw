import pandas as pd
import numpy as np
from keras.models import Sequential #순차모델, 선형으로 레이어 쌓기
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from sklearn.metrics import precision_score, recall_score, f1_score
from keras.utils import np_utils

from sklearn.model_selection import train_test_split

# get data from csv file
data = pd.read_csv('as3.csv')
data1 = np.array(data)

# split x and y from data
X = list(map(lambda x: x[1:], data1))
Y = list(map(lambda x: x[0]-1, data1))

# train/test/validation random split 작성
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.25)

# the name of class(label)
cifar10_label = ['horeca','retail'] #str, for printing
label_to_calculate = [0,1] #int, real label value

# change python list to numpy array
X_train = np.asarray(x_train)
X_test = np.asarray(x_test)
X_valid = np.asarray(x_valid)

Y_train = np.array(y_train)
Y_test = np.asarray(y_test)
Y_valid = np.asarray(y_valid)

# change numpy array shape [sample, features]
# to [sample, row, columns(features), channels] 작성
train_data = X_train.reshape(-1, 1, 7, 1)
test_data = X_test.reshape(-1, 1, 7, 1)
validation_data = X_valid.reshape(-1, 1, 7, 1)

# transform Y to one hot vector 작성
train_label = np_utils.to_categorical(Y_train)
test_label = np_utils.to_categorical(Y_test)
validation_label = np_utils.to_categorical(Y_valid)

# total number of class(label) 작성
num_classes = test_label.shape[1]

# 하단에 나머지 작성

def cnn_model():
    #define model
    model = Sequential()
    model.add(Conv2D(16, kernel_size=(1,4), input_shape=(1, 7, 1), activation='relu')) # tanh or sigmoid or relu
    model.add(MaxPooling2D(pool_size=(1,2)))
    model.add(Dropout(0.5))    #overfitting 방지
    model.add(Flatten()) #1차원화 시키기 , 전결합층에 넣기전에 필요한 작업
    model.add(Dense(16, activation='relu')) # Dense로 전결합층의 심츨 신경망 생성
    model.add(Dense(num_classes, activation='softmax')) #Softmax로 클래스 분류
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# build & model
model = cnn_model()
print(model.summary()); print('\n')

# Fit the model (train 5000 data, validate 1000 data)
model.fit(train_data, train_label, validation_data=(validation_data, validation_label), epochs=10, batch_size=128, verbose=1)

# Evaluation of the model (on 1000 set of test data)
print('\nEvaluation')
scores = model.evaluate(test_data, test_label, verbose=1)

# Prediction of the model (on 1000 set of test data)
print('\nPrediction')
y_pred = model.predict(test_data, verbose=1)
Y_pred = np.argmax(y_pred, axis=1)

# Calculate Scores (on 1000 set of test data)
print('\nCNN on mnist')
prec = precision_score(np.argmax(test_label, axis=1), Y_pred, labels=label_to_calculate, average=None)
rec = recall_score(np.argmax(test_label, axis=1), Y_pred, labels=label_to_calculate, average=None)
f1 = f1_score(np.argmax(test_label, axis=1), Y_pred, labels=label_to_calculate, average=None)
prf = pd.DataFrame([prec, rec, f1], columns=cifar10_label, index=['Precision', 'Recall', 'F1'])
print(prf.iloc[0], '\n'); print(prf.iloc[1],'\n'); print(prf.iloc[2], '\n')
print("\nTotal Accuracy: {:.2f}".format(scores[1]*100))
