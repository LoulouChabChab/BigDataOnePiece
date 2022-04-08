import math
# import required module
import os

import matplotlib.pyplot as plot
import numpy
from PIL import Image
from sklearn.cluster import KMeans

# assign directory
directory = 'Data/Robin'
index = 0


# iterate over files in
# that directory
def data(file):
    image = Image.open(file)
    # extract other basic metadata
    info_dict = {
        "Filename": image.filename,
        "Image Height": image.height,
        "Image Width": image.width
    }

    for label, value in info_dict.items():
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
    for i in range(nbColors):
        print("Couleur ", i, " : ")
        print('#%02x%02x%02x' % (math.ceil(clusters.cluster_centers_[i][0]), math.ceil(clusters.cluster_centers_[i][1]),
                                 math.ceil(clusters.cluster_centers_[i][2])))
        barlist[i].set_color('#%02x%02x%02x' % (
            math.ceil(clusters.cluster_centers_[i][0]),
            math.ceil(clusters.cluster_centers_[i][1]),
            math.ceil(clusters.cluster_centers_[i][2])))
    plot.show()


for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        data(f)

# df = pd.DataFrame()
# df.to_csv('mystake.csv', mode='a', header=False)

# # extract EXIF data
# exifdata = image.getexif()
#
#
#
# # iterating over all EXIF data fields
# for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes
#     if isinstance(data, bytes):
#         data = data.decode()
#     print(f"{tag:25}: {data}")
