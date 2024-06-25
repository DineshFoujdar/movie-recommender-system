import streamlit as st
import pickle
import pandas as pd
import requests

#def fetch_poster(movie_id):
 #   response = requests.get('https://api.themoviedb.org/3/movie/{}/?api_key=49974f34fdbfafc6f5d0681e64b472d9&language=en-US'.format(movie_id))
  #  data = response.json()
   # return"http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
   # recommended_movie_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id


        recommended_movie.append(movies.iloc[i[0]].title)
       # recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie

# Load the movie dictionary from pickle file
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert dictionary to DataFrame
movies = pd.DataFrame(movies_dict)

# Streamlit app title
st.title('Movie Recommender System')

option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):

    names = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image('http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg')
    with col2:
        st.text(names[1])
        st.image('http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg')
    with col3:
        st.text(names[2])
        st.image('http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg')
    with col4:
        st.text(names[3])
        st.image('http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg')
    with col5:
        st.text(names[4])
        st.image('http://image.tmdb.org/t/p/w500/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg')




