import tensorflow as tf
#from tensorflow import keras
from keras import layers
import numpy as np
import pandas as pd


'''

np.set_printoptions(precision=3, suppress=True)

modelData = pd.read_csv("Airline_Delay_Cause_No_Extra_Info.csv")
modelData.head()

modelDataCopy = modelData.copy()

inputData = {}

for name, column in modelDataCopy.items():
    dtype = column.dtype
    if dtype == object:
        dtype = tf.string
    else:
        dtype = tf.float32
    inputData[name] = tf.keras.Input(shape=(1,), name=name, dtype=dtype)

numeric_inputs = {name:input for name, input in inputData.items() if input.dtype == tf.float32}

x = layers.Concatenate()(list(numeric_inputs.values()))
normx = layers.Normalization()
normx.adapt(np.array(modelData[numeric_inputs.keys()]))
all_numeric_inputs = normx(x)

preprocessed_inputs = [all_numeric_inputs]

for name, input in inputData.items():
  if input.dtype == tf.float32:
    continue

  lookup = layers.StringLookup(vocabulary=np.unique(modelDataCopy[name]))
  one_hot = layers.CategoryEncoding(num_tokens=lookup.vocabulary_size())

  x = lookup(input)
  x = one_hot(x)
  preprocessed_inputs.append(x)

preprocessed_inputs_cat = layers.Concatenate()(preprocessed_inputs)

flightDelay_preprocessing = tf.keras.Model(inputData, preprocessed_inputs_cat)

#tf.keras.utils.plot_model(model = flightDelay_preprocessing , rankdir="LR", dpi=72, show_shapes=True)

modelDataCopy_dict = {name: np.array(value) for name, value in modelDataCopy.items()}
#print(modelDataCopy_dict)
copy_dict = {name:values[:1] for name, values in modelDataCopy_dict.items()}
flightDelay_preprocessing(copy_dict)

'''
def initial_training_function(newhistoricaldata, modelsavename):
  historical_data = pd.read_csv(newhistoricaldata + '.csv')
  arr_labels = historical_data.pop('arr_del15') #Make a model for the total flights and total delayed flights and come up with a percentage value that determines if the flight will be delay based on the data and compare it to the current whether to verify.
  data_arr = np.array(historical_data)
  arr_labels2 = np.array(arr_labels)
  #print(data_arr)
  normalized_arr = (data_arr - np.min(data_arr)) / (np.max(data_arr) - np.min(data_arr))
  #print(normalized_arr)
  normalized_arr_labels = (arr_labels2 - np.min(arr_labels2)) / (np.max(arr_labels2) - np.min(arr_labels2))
  #print(normalized_arr_labels)


  flightDelay_model = tf.keras.Sequential([layers.Dense(10), layers.Dense(60), layers.Dense(60), layers.Dense(1)])

  flightDelay_model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=["accuracy"],optimizer=tf.keras.optimizers.Adam())

  flightDelay_model.fit(x=normalized_arr, y=normalized_arr_labels, epochs=20)

  flightDelay_model.save(modelsavename + '.keras')

#def loaded_training_function(modelsavename):
  loaded_model = tf.keras.models.load_model(modelsavename + '.keras')
  loss, acc = loaded_model.evaluate(normalized_arr, normalized_arr_labels, verbose=2)
  #print(loss)
  while(acc <= 0.0003):
    loaded_model = tf.keras.models.load_model(modelsavename + '.keras')
    loss, acc = loaded_model.evaluate(normalized_arr, normalized_arr_labels, verbose=2)
    loaded_model.fit(x=normalized_arr, y=normalized_arr_labels, epochs=20)
    loaded_model.save(modelsavename + '.keras')
    #print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))
  #print("Ready for Prediction.")
  #print(loss)

  final_model = tf.keras.models.load_model(modelsavename + '.keras')
  result = final_model.predict(data_arr)
  count = 0
  for arr in result:
    for inner_arr in arr:
      count += abs(inner_arr)
  count /= arr
  print(abs(count))
'''
def prediction_function():
  input_data = pd.read_csv('Book1.csv')
  final_model = tf.keras.models.load_model('test.keras')
  result = final_model.predict(input_data)
  
'''