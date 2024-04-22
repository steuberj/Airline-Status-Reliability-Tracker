import tensorflow as tf
from keras import layers
import numpy as np
import pandas as pd

def training_function(newhistoricaldata, modelsavename, ytargetdata):
  global data_arr
  historical_data = pd.read_csv(newhistoricaldata + '.csv')
  arr_labels = historical_data.pop(ytargetdata) #Make a model for the total flights and total delayed flights and come up with a percentage value that determines if the flight will be delay based on the data and compare it to the current whether to verify.
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
  final_model = tf.keras.models.load_model(loadModelName + '.keras')
  result = final_model.predict(data_arr)
  count = 0
  for arr in result:
    for inner_arr in arr:
      count += abs(inner_arr)
  count /= arr
  return count

def probabilityCalc(modelsavenamex, modelsavenamey):
  averageDelays = runModel(modelsavenamex)
  averageFlights = runModel(modelsavenamey)
  delayProbability = (averageDelays[0] / averageFlights[0]) * 100
  if delayProbability > 80:
    delayProbability /= 2.5
    return('Probability: ' + str(delayProbability))
  elif delayProbability > 50:
    delayProbability /= 2
    return('Probability: ' + str(delayProbability))
  else:
    return('Probability: ' + str(delayProbability))

def controlFunction(modelSaveNamex, modelSaveNamey):
  print(probabilityCalc(modelSaveNamex, modelSaveNamey))