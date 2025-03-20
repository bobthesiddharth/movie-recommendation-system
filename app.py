import pickle
import streamlit as st
import requests
import pandas as pd

# Load movie dataset and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API Key (Replace with your actual API key)
API_KEY = "204ca9fbda56438daf27cf017be44936"

# TMDB Image Base URL
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Placeholder image in case no poster is found
PLACEHOLDER_IMAGE = "https://via.placeholder.com/500x750?text=No+Image"


def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API with error handling."""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Get poster path safely
        poster_path = data.get('poster_path')
        return f"{TMDB_IMAGE_BASE_URL}{poster_path}" if poster_path else PLACEHOLDER_IMAGE

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return PLACEHOLDER_IMAGE  # Use fallback image


def recommend(movie):
    """Find the top 5 recommended movies based on cosine similarity."""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []

        for i in distances[1:6]:  # Get top 5 similar movies
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))  # Fetch poster
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        print(f"Error in recommend(): {e}")
        return [], []


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie", movie_list)

# Show recommendations when button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Display recommended movies in 5 columns
    if recommended_movie_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[idx])
                st.image(recommended_movie_posters[idx], width=150)
    else:
        st.error("No recommendations found. Try another movie!")

# Ensure sklearn is installed
try:
    from sklearn.feature_extraction.text import CountVectorizer
except ModuleNotFoundError:
    st.error("scikit-learn is not installed. Install it using: `pip install scikit-learn`")