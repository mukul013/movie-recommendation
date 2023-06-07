import requests
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://downloads.magicanoz.com/1:/desktop-1920x1080%20copy.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movie_poster = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))

    return recommended_movies,recommended_movie_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

new_title = '<p style="font-weight:bold; font-family:sans-serif; color:white; font-size: 42px; text-align: center">Movie Recommender System</p>'
st.markdown(new_title, unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    '',
    movies['title'].values)

st.text(" ")
st.text(" ")


m = st.markdown("""
<style>
div.stButton > button:first-child {
     margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background-color: #E50914;
    font-size: 25px;
    
}
</style>""", unsafe_allow_html=True)


if st.button('Recommend'):
    st.text(" ")
    st.text(" ")
    names,posters = recommend(selected_movie_name)
    col1, col2, col3 ,col4,col5= st.columns(5 , gap="medium")

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col1:
        st.text(names[5])
        st.image(posters[5])

    with col2:
        st.text(names[6])
        st.image(posters[6])

    with col3:
        st.text(names[7])
        st.image(posters[7])

    with col4:
        st.text(names[8])
        st.image(posters[8])

    with col5:
        st.text(names[9])
        st.image(posters[9])

