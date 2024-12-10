import pandas as pd
import pickle 
import streamlit as st
import requests

def load_model():
    try:
        with open('Recommendation_system.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("Model not found. Please train the model first.")
        return None

def load_data():
    try:
        with open('recommendation_data.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("Data not found. Please preprocess the data first.")
        return None
        

data = load_data()
model = load_model()



def fetch_images(movie_id = None):
    # API details
    api_key = "2d93afa4fe9bcb72ba4e36370e670b79"
    language = "en-US"

    # Construct the URL
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"

    # Make the API request
    insert_id_inUrl = url.format(movie_id = movie_id)
    response = requests.get(insert_id_inUrl, params={"api_key": api_key})

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        poster = data['posters'][0]
        poster_file_path = poster['file_path']
        Full_image_url = f"https://image.tmdb.org/t/p/w500/{poster_file_path}" 
        return Full_image_url
    else:
        print(f"Error: {response.status_code}")








def movies_similarity(title):
    try:
        recommended_movies = []
        recommended_movies_poster = []
        indx = data[data['title'] ==  title].index
        similar_array = model[indx][0]
        fivesimilar_movies= sorted(list(enumerate(similar_array)), reverse = True, key = lambda x: x[1])[1:6]
        
        for i, score in fivesimilar_movies:
            movies_title = data.iloc[i]['title']
            movies_ids = data.iloc[i]['id']
            images_path = fetch_images(movies_ids)
            
            recommended_movies.append(movies_title)
            recommended_movies_poster.append(images_path)
        return recommended_movies, recommended_movies_poster
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None



st.title("Movies Recommendation system")

selected_movies = st.selectbox('Enter your favorite movie', data['title'])


if st.button('Recommendation'):
        title, posters = movies_similarity(selected_movies)
        st.subheader("Recommended Movies:")
        for i in title:

            col1, col2, col3, col4, col5 = st.columns(5) # , col6, col7

        with col1:
            st.markdown(f"#### {title[0]}")  # Use H3 for smaller text
            st.image(posters[0])

        with col2:
            st.markdown(f"#### {title[1]}")  # Use H3 for smaller text
            st.image(posters[1])

        with col3:
            st.markdown(f"#### {title[2]}")  # Use H3 for smaller text
            st.image(posters[2])

        with col4:
            st.markdown(f"#### {title[3]}")  # Use H3 for smaller text
            st.image(posters[3])

        with col5:
            st.markdown(f"#### {title[4]}")  # Use H3 for smaller text
            st.image(posters[4])


