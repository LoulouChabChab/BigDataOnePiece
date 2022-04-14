# Import Pandas
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plot
import numpy as np

# Load Movies Metadata
from sklearn.metrics.pairwise import linear_kernel


metadata = pd.read_csv('data_latest.csv', low_memory=False)

font1 = {'color': 'black', 'fontweight': 'bold'}

groupByFaction = metadata["Faction"].value_counts()
print(groupByFaction)

groupByFaction.plot(kind='pie', autopct=lambda x: str(round(x, 2)) + '%')
plot.title("Group By faction", fontdict=font1)
plot.xlabel("Faction", fontdict=font1)
plot.ylabel("Count", fontdict=font1)
plot.show()
print("-----------------------------------")

top5Colors1 = metadata['Couleur 1'].value_counts()
top5Colors1 = top5Colors1.nlargest(n=5)
color = ['#2F4F4F', 'black', '#F5F5F5', '#D3D3D3', '#a9a9a9']
plot.gcf().subplots_adjust(bottom=0.3)
plot.title("Top 5 Colors1", fontdict=font1)
plot.xlabel("Colors", fontdict=font1)
plot.ylabel("Count", fontdict=font1)
top5Colors1.plot(kind='bar', color=color)
plot.show()

print("-----------------------------------")

top10Colors1 = metadata['Couleur 1'].value_counts()
print(top10Colors1.nlargest(n=10))
print("-----------------------------------")

top10Colors2 = metadata['Couleur 2'].value_counts()
print(top10Colors2.nlargest(n=10))
print("-----------------------------------")

UnionTop10Colors = pd.concat([top10Colors1, top10Colors2]).drop_duplicates()
UnionTop10Colors = UnionTop10Colors.nlargest(n=10)
print(UnionTop10Colors)
plot.gcf().subplots_adjust(bottom=0.3)
plot.title("Top 10 colors", fontdict=font1)
plot.xlabel("Color", fontdict=font1)
plot.ylabel("Count", fontdict=font1)
UnionTop10Colors.plot(kind='bar')
plot.show()
print("-----------------------------------")

groupByFruits = metadata["Fruits démon"].value_counts()
print(groupByFruits)
plot.figure().autofmt_xdate(rotation=45)
plot.gcf().subplots_adjust(bottom=0.25)
plot.title("Group by fruit", fontdict=font1)
plot.xlabel("Fruits", fontdict=font1)
plot.ylabel("Count", fontdict=font1)

groupByFruits.plot(kind='bar')
plot.show()
