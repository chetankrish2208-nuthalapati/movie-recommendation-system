# Movie Recommendation System Using Similarity

A beginner-level machine learning project that recommends movies based on their similarity to a movie selected by the user.

## Project Overview

This project uses a simple content-based recommendation approach to find movies that are similar to a selected movie.

The system uses:

* Movie genre
* Release year

These features are converted into numerical representations using **TF-IDF**, and **Cosine Similarity** is then used to measure how similar the movies are.

## Dataset

The project uses a custom dataset created for educational purposes.

The dataset contains **50 movies** with the following columns:

* `MovieID`
* `Title`
* `Genre`
* `Rating`
* `Year`

## How It Works

The recommendation process follows these steps:

1. Load the movie dataset.
2. Combine the movie genre and release year into a feature.
3. Convert the feature text into numerical values using TF-IDF.
4. Calculate the cosine similarity between all movies.
5. Take the movie entered by the user.
6. Find the movies with the highest similarity scores.
7. Display the top 5 recommendations.

## Example

If the user enters:

```text
Inception
```

The system finds movies with similar genre and year characteristics and displays the top 5 recommendations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

## Machine Learning Methods

### TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts text-based features into numerical values that can be used for similarity calculations.

### Cosine Similarity

Cosine similarity measures how similar two feature vectors are.

The similarity score is then used to identify movies that are closest to the selected movie.

## Limitations

* The dataset contains only 50 movies.
* The dataset is a custom educational dataset.
* Recommendations are based only on genre and release year.
* User preferences and viewing history are not considered.
* The system does not use advanced recommendation techniques such as collaborative filtering.

## Learning Outcome

This project helped me practice:

* Python programming
* Data handling with Pandas
* Feature extraction using TF-IDF
* Cosine similarity
* Basic recommendation systems
* Working with machine-learning libraries

## Project Structure

```text
Movie-Recommendation-System
├── movie_dataset.ods
├── moive_recommendation.py
└── README.md
```
