import tensorflow as tf 
from tensorflow import keras
import numpy as np

model = keras.sequential([ keras.layers.dense(units =1, input_shape =[1])])
model.compile(optimizer = 'sgd',loss = 'mean_squared_error')

XS = np.array([],dtype = float)
YS = np.array([],dtype = float)

model.fit(XS,YS,epochs = 500)
print(model.predict([10.0]))