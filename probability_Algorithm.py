import tensorflow as tf
from keras import layers
import numpy as np
import pandas as pd

def training_function(newhistoricaldata, modelsavename, ytargetdata):
  global data_arr
  historical_data = pd.read_csv(newhistoricaldata + '.csv')
  arr_labels = historical_data.pop(ytargetdata)
  data_arr = np.array(historical_data)
  arr_labels2 = np.array(arr_labels)
  normalized_arr = (data_arr - np.min(data_arr)) / (np.max(data_arr) - np.min(data_arr))
  normalized_arr_labels = (arr_labels2 - np.min(arr_labels2)) / (np.max(arr_labels2) - np.min(arr_labels2))
  counter = 0
  while(counter < 1):
    if(counter == 0):
      flightDelay_model = tf.keras.Sequential([layers.Dense(10), layers.Dense(60), layers.Dense(60), layers.Dense(1)])
      flightDelay_model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam())
      flightDelay_model.fit(x=normalized_arr, y=normalized_arr_labels, epochs=20)
      flightDelay_model.save(modelsavename + '.keras')
    else:
      loaded_model = tf.keras.models.load_model(modelsavename + '.keras')
      loaded_model.fit(x=normalized_arr, y=normalized_arr_labels, epochs=20)
      loaded_model.save(modelsavename + '.keras')
    counter += 1

def runModel(loadModelName):
  global data_arr
  final_model = tf.keras.models.load_model(loadModelName + '.keras')
  result = final_model.predict(data_arr)
  count = 0
  for arr in result:
    for inner_arr in arr:
      count += abs(inner_arr)
  count /= abs(arr)
  return count

def probabilityCalc(modelsavenamex, modelsavenamey):
  averageDelays = runModel(modelsavenamex)
  averageFlights = runModel(modelsavenamey)
  delayProbability = (averageDelays[0] / averageFlights[0]) * 100
  if delayProbability > 80:
    delayProbability /= 2.5
    if delayProbability > 60:
      return 'Delayed'
    elif delayProbability > 45:
      return 'Possible Delay'
    else:
      return 'On-Time'
  elif delayProbability > 50:
    delayProbability /= 2
    if delayProbability > 60:
      return 'Delayed'
    elif delayProbability > 45:
      return 'Possible Delay'
    else:
      return 'On Time'
  else:
    if delayProbability > 60:
      return 'Delayed'
    elif delayProbability > 45:
      return 'Possible Delay'
    else:
      return 'On Time'

def controlFunction(modelSaveNamex, modelSaveNamey):
  return(probabilityCalc(modelSaveNamex, modelSaveNamey))