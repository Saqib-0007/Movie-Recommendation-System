import streamlit as st
import pickle
import requests

# 🔑 your actual API key (DON'T overwrite this)
API_KEY = "858d2afecb1becfd5a806ed3e9a9740a"


# 🎬 fetch poster using movie title (works even if movie_id is wrong)
def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    data = requests.get(url).json()

    if data.get('results'):
        poster_path = data['results'][0].get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    return "https://via.placeholder.com/500x750?text=No+Image"


# 🎯 recommend function
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_sorted = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_sorted:
        title = movies_list.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_movies, recommended_posters


# 📂 load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = movies_list['title'].values


# 🎨 UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie", movies)


# 🚀 button
if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    st.write("### Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])