import json
import numpy as np
from keras import layers
from keras import models
from keras.layers.normalization import BatchNormalization
from keras.models import model_from_json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def nn_prediction(X_test):
    '''predicting with predicted model'''
    with open('../models/2_nn.json','r') as f:
        model_json = json.load(f)

    model = model_from_json(model_json)
    model.load_weights('../models/2_nn.h5')
    print('Model loaded')
    predictions = model.predict(X_test)
    return predictions

def nnModel(df):
    '''training model'''
    number_classes = len(set(df['name']))

    y_names=df['name']
    le = preprocessing.LabelEncoder()
    le.fit(y_names)

    y=np.vstack(le.transform(y_names))
    X=np.vstack(df['features'])
    np.save('class_names2.npy', le.classes_)

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

    inshape=(X_train.shape[1],)
    model = models.Sequential()
    model.add(layers.Dense(512, activation='relu', input_shape=inshape))
    model.add(layers.Dense(256, activation='relu'))

    model.add(BatchNormalization())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(number_classes, activation='softmax'))
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    model.fit(X_train,
            y_train,
            epochs=60,
            batch_size=50,
            validation_data=(X_test, y_test))

    results = model.evaluate(X_test, y_test)
    print("")
    print(results)
    print("\n")

    predictions = model.predict(X_test)
    print(predictions)

    print(model)
    name='../models/2_nn'

    model_json = model.to_json()
    with open(name+'.json', "w") as json_file:
        json.dump(model_json, json_file)

    model.save_weights(name+'.h5')
    return