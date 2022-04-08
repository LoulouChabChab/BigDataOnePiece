import math
# import required module
#pil
import os
import csv
import matplotlib.pyplot as plot
import numpy
from PIL import Image
from sklearn.cluster import KMeans

# assign directory
directory = 'Data'
index = 0


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
        data.append('#%02x%02x%02x' % (
            math.ceil(clusters.cluster_centers_[i][0]), math.ceil(clusters.cluster_centers_[i][1]),
            math.ceil(clusters.cluster_centers_[i][2])))
        barlist[i].set_color('#%02x%02x%02x' % (
            math.ceil(clusters.cluster_centers_[i][0]),
            math.ceil(clusters.cluster_centers_[i][1]),
            math.ceil(clusters.cluster_centers_[i][2])))
    plot.show()
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
