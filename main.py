# Import Pandas
import pandas as pd
from matplotlib import pyplot as plt
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import linear_kernel

# Load Movies Metadata
metadata = pd.read_csv('data_OP.csv', low_memory=False)

# Display some stats
print("Total number of images : ", metadata.shape[0])
print("Total number of unique characters : ", metadata["Personnage"].nunique())
print("Total number of unique color 1 types : ", metadata["Couleur 1"].nunique())
print("Total number of unique color 2 types : ", metadata["Couleur 2"].nunique())
print(metadata["Personnage"].value_counts())

# print(metadata['Couleur 1'].head())
# print(metadata.shape)
# cosine_sim = linear_kernel(metadata, metadata)

# values = array(metadata)
# print(values[0][4])
# # integer encode
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(values[0])
# print(integer_encoded)
# # binary encode
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# print(onehot_encoded)
# # invert first example
# inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
# print(inverted)
