import pandas as pd
from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

image = Image.open("Data/Ace/75.png")
# extract other basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Height": image.height,
    "Image Width": image.width
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")


numarray = numpy.array(image.getdata(), numpy.uint8)
clusters = KMeans(n_clusters=3)
clusters.fit(numarray)
npbins = numpy.arange(0, 4)
histogram = numpy.histogram(clusters.labels_, bins=npbins)
labels = numpy.unique(clusters.labels_)
barlist = plot.bar(labels, histogram[0])
for i in range(3):
    barlist[i].set_color('#%02x%02x%02x' % (
        math.ceil(clusters.cluster_centers_[i][0]),
        math.ceil(clusters.cluster_centers_[i][1]),
        math.ceil(clusters.cluster_centers_[i][2])))
plot.show()

df = pd.DataFrame()
df.to_csv('mystake.csv', mode='a', header=False)
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
