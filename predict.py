import pandas as pd
import pickle
import tensorflow as tf

import numpy as np
import os
from helper_function import pre_processing,tokenization
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import argparse

# loading the tokenized object
msg = "Please Pass the test file"
parser = argparse.ArgumentParser(description=msg)
parser.add_argument('--file', dest='file', required=True)
args = parser.parse_args()
test_file = args.file
test_df = pd.read_csv(test_file)
try:
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
except FileNotFoundError:
    print("Please check the Tokenizer.pickle file is avaibale at the given location ")

#loading the save keras model
try:
    model = tf.keras.models.load_model("my_model")
    print("Model ")
except:
    print("Model saved not found ")

pre_process_data=pre_processing(test_df)  # output as a DF preproceed data
sequence_data=tokenization(pre_process_data,tokenizer)

y_pred=model.predict(sequence_data)
test_df["label"]=(np.rint(y_pred)).astype(int)
test_df[['id', 'label']].to_csv("test_output.csv")
print(f"Output file is genrated at {os.getcwd()}")