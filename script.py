import csv
import math
# import required module
# pil
import os

import git

pathGit = "https://github.com/LoulouChabChab/BigDataOnePiece.git"
pathDesk = "C://"

git.Git(pathDesk).clone(pathGit)

import matplotlib.pyplot as plot
import numpy
from PIL import Image
from sklearn.cluster import KMeans
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

# assign directory
directory = pathDesk + "BigDataOnePiece/Data"
print(directory)

# assign directory
#directory = 'Data'
index = 0


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


# iterate over files in
# that directory
def data(file):
    data = []
    image = Image.open(file)
    # extract other basic metadata
    info_dict = {
        "Filename": image.filename,
        "Image Height": image.height,
        "Image Width": image.width
    }

    for label, value in info_dict.items():
        data.append(value)
        print(f"{label:25}: {value}")

    nbColors = 2
    numarray = numpy.array(image.getdata(), numpy.uint8)
    clusters = KMeans(n_clusters=nbColors)
    if numarray.ndim == 1:
        return
    clusters.fit(numarray)
    npbins = numpy.arange(0, nbColors + 1)
    print(npbins)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)
    labels = numpy.unique(clusters.labels_)
    barlist = plot.bar(labels, histogram[0])

    f = open('data2.csv', 'a')
    writer = csv.writer(f)

    for i in range(nbColors):
        data.append(convert_rgb_to_names((math.ceil(clusters.cluster_centers_[i][0]),
                                          math.ceil(clusters.cluster_centers_[i][1]),
                                          math.ceil(clusters.cluster_centers_[i][2]))))
        barlist[i].set_color('#%02x%02x%02x' % (
            math.ceil(clusters.cluster_centers_[i][0]),
            math.ceil(clusters.cluster_centers_[i][1]),
            math.ceil(clusters.cluster_centers_[i][2])))
    # plot.show()
    writer.writerow(data)


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(directory)
    elif os.path.isdir(f):
        # print(f)
        for filename2 in os.listdir(f):
            f2 = os.path.join(f, filename2)
            data(f2)

# df = pd.DataFrame()

