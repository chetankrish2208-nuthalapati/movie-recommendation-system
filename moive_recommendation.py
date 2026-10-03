import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_excel("movie_dataset.ods", engine="odf")

# Create features
movies["Features"] = movies["Genre"] + " " + movies["Year"].astype(str)

# Convert features into numbers
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(movies["Features"])

# Calculate similarity
similarity = cosine_similarity(feature_matrix)


# Recommendation function
def recommend_movie(movie_title):

    matching_movies = movies[
        movies["Title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        print("\nMovie not found in the dataset.")
        return

    movie_index = matching_movies.index[0]

    similarity_scores = list(enumerate(similarity[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended movies:")

    for index, score in similarity_scores[1:6]:
        percentage = score * 100
        print(f"{movies.iloc[index]['Title']} - Similarity: {percentage:.1f}%")


# User input
movie_name = input("\nEnter a movie name: ")

recommend_movie(movie_name)
