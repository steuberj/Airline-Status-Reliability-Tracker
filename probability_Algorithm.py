import tensorflow as tf
#from tensorflow import keras
from keras import layers
import numpy as np
import pandas as pd

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

copy_dict = {name:values[:1] for name, values in modelDataCopy_dict.items()}
