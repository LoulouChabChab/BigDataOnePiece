
import pandas as pd

import matplotlib.pyplot as plot

metadata = pd.read_csv('CSV/Analyze.csv', low_memory=False)

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

colorValue = []
colorName = []
colorCount = []
for i in range(10):
    for j in range(10):
        if top10Colors1.index.tolist()[i] == top10Colors2.index.tolist()[j]:
            colorValue.append(
                [top10Colors1.index.tolist()[i], top10Colors1.nlargest(n=10)[i] + top10Colors2.nlargest(n=10)[j]])

print('#######################################################')
colorValue.sort(key=lambda x: x[1])
colorValue.reverse()
for i in range(len(colorValue)):
    colorName.append(colorValue[i][0])
    colorCount.append(colorValue[i][1])
    print([colorValue[i][0]], ' ', colorValue[i][1])
print('#######################################################')
c = ['#2F4F4F', 'black', '#F5F5F5', '#696969', '#DCDCDC', '#C0C0C0', '#D3D3D3', '#a9a9a9']
ax = plot.figure(figsize=(9, 9))
plot.bar(colorName, colorCount, color=c)
plot.gcf().subplots_adjust(bottom=0.3)
plot.title("Top 10 colors", fontdict=font1)
plot.xlabel("Color", fontdict=font1)
plot.ylabel("Count", fontdict=font1)
plot.show()
print("-----------------------------------")

groupByFruits = metadata["Fruit"].value_counts()
print(groupByFruits)
plot.figure().autofmt_xdate(rotation=45)
plot.gcf().subplots_adjust(bottom=0.25)
plot.title("Group by fruit", fontdict=font1)
plot.xlabel("Fruit", fontdict=font1)
plot.ylabel("Count", fontdict=font1)

groupByFruits.plot(kind='bar')
plot.show()
