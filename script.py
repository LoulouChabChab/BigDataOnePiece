import math
import os
import numpy
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

import git
pathGit = "https://github.com/LoulouChabChab/BigDataOnePiece.git"
pathDesk = "C://"
git.Git(pathDesk).clone(pathGit)
# assign directory
directory = pathDesk + "BigDataOnePiece/Data"
# directory = 'Data'
indexRow = 0
data_filename = []
data_overview = []

df_init = pd.read_csv('data_init.csv', low_memory=False)


def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]


def get_size(height, width):
    if height + width > 350:
        mySize = "Small"
    else:
        mySize = "ExtraSmall"
    if height + width > 500:
        mySize = "Medium"
    if height + width > 750:
        mySize = "Large"
    if height + width > 1000:
        mySize = "ExtraLarge"
    if height + width > 2000:
        mySize = "ExtraExtraLarge"
    return mySize


# iterate over files in
# that directory
def create_csv(file, indexRow):
    overview = ''
    image = Image.open(file)

    # Kmeans
    nbColors = 2
    numarray = numpy.array(image.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters=nbColors)
    if numarray.ndim == 1:
        return
    clusters.fit(numarray)

    # extract other basic metadata
    if image.filename is None:
        return
    data_filename.append(image.filename)
    overview += get_size(image.height, image.width) + ' '

    if "inverted" in filename:
        overview += " inverted inverted "
    else:
        for i in range(nbColors):
            overview += convert_rgb_to_names((math.ceil(clusters.cluster_centers_[i][0]),
                                              math.ceil(clusters.cluster_centers_[i][1]),
                                              math.ceil(clusters.cluster_centers_[i][2]))) + ' '

    overview += df_init['Personnage'].iloc[indexRow] + ' ' + df_init['Sexe'].iloc[indexRow] + ' ' + \
                df_init['Faction'].iloc[indexRow] + ' ' + df_init['Fruits'].iloc[indexRow]
    data_overview.append(overview)


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
    elif os.path.isdir(f):
        for filename2 in os.listdir(f):
            f2 = os.path.join(f, filename2)
            create_csv(f2, indexRow)
            print(f2, ' ', indexRow)
            indexRow += 1

data = {'Filename': data_filename,
        'Overview': data_overview}
df = pd.DataFrame(data)
df.to_csv('data_full.csv')
