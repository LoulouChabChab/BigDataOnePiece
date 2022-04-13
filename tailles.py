# Import Pandas
import numpy as np
import pandas as pd

i = 0
metadata = pd.read_csv('data.csv', low_memory=False)
metadata = metadata.reset_index()  # make sure indexes pair with number of rows
new_col = ['Taille']
for index in metadata.iterrows():
    size = metadata["Height"] + metadata["Width"]
    mySize = ""
    if size[i] > 350:
        mySize = "S"
    else:
        mySize = "XS"
    if size[i] > 500:
        mySize = "M"
    if size[i] > 750:
        mySize = "L"
    if size[i] > 1000:
        mySize = "XL"
    if size[i] > 2000:
        mySize = "XXL"
    df = pd.read_csv("overview.csv")
    df['Taille'].iloc[i] = mySize
    df.to_csv("overview.csv", index=False)
    print(size[i], mySize)
    print("----------------------------")
    i += 1
