# Import Pandas
import pandas as pd

# Load Movies Metadata
from sklearn.metrics.pairwise import linear_kernel

metadata = pd.read_csv('test.csv', low_memory=False)

# print(metadata['Couleur 1'].head())
# print(metadata.shape)
# cosine_sim = linear_kernel(metadata, metadata)


from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
values = array(metadata)
print(values[0][4])
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values[0])
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted)
