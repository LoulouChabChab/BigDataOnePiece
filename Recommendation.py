import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load Movies Metadata
metadata = pd.read_csv('CSV/data_full.csv', low_memory=False)

tfidf = TfidfVectorizer()
metadata['Overview'] = metadata['Overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(metadata['Overview'])
# print(tfidf_matrix.shape)
# print(tfidf.get_feature_names_out())
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# print(cosine_sim.shape)
# print(cosine_sim[1])
indices = pd.Series(metadata.index, index=metadata['Filename']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    if title in indices.index:
        # Get the index of the image
        idx = indices[title]
    else:
        return None

    # Get the scores of all images
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the images based on the scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10
    sim_scores = sim_scores[1:21]

    # Get the image indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10
    return metadata['Filename'].iloc[movie_indices]


# Example 1
# path = "C://BigDataOnePiece/Images\\"
# personnage = "Shanks"
# image = "5.png_inverted.png"

# Example 2
path = "C://BigDataOnePiece/Images\\"
personnage = "Kizaru"
image = "Kizaru1.jpeg"

complete_path = path + personnage + "\\" + image

recommendation = get_recommendations(complete_path)

if recommendation is not None:
    img = mpimg.imread(complete_path)
    imgplot = plt.imshow(img)
    plt.show()

    for i in range(3):
        img = mpimg.imread(recommendation.iloc[i])
        imgplot = plt.imshow(img)
        plt.show()

    recommendation.to_csv('CSV/data_recommendation.csv')
else:
    print("No image found !")
