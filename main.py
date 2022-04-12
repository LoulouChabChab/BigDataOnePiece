# Import Pandas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Movies Metadata
from sklearn.metrics.pairwise import linear_kernel

metadata = pd.read_csv('data_latest.csv', low_memory=False)

# Display some stats
print("Total number of images : ", metadata.shape[0])
print("Total number of unique characters : ", metadata["Personnage"].nunique())
print("Total number of unique color 1 types : ", metadata["Couleur 1"].nunique())
print("Total number of unique color 2 types : ", metadata["Couleur 2"].nunique())
print(metadata["Personnage"].value_counts())
print("-----------------------------------")
tfidf = TfidfVectorizer()
metadata['Overview'] = metadata['Overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(metadata['Overview'])
print(tfidf_matrix.shape)
print(tfidf.get_feature_names_out())
print("-----------------------------------")
# print(metadata['Couleur 1'].head())
# print(metadata.shape)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)
print(cosine_sim[1])
indices = pd.Series(metadata.index, index=metadata['Filename']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['Filename'].iloc[movie_indices]


print("-----------------------------------")
recommandation = get_recommendations('Data/Yamato/one-piece-yamato-758x392.jpg')
print(recommandation)
