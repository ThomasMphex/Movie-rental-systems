import streamlit as st
import csv
from PIL import Image
import base64
import os

def check_movie_exists(movie_title, movies_file):
    with open(movies_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == movie_title:
                return True
    return False

# def convert_image_to_link(poster_image):
#     if poster_image is not None:
#         img = Image.open(poster_image)
#         img_bytes = img.tobytes()
#         img_base64 = base64.b64encode(img_bytes).decode('utf-8')
#         img_link = f"data:image/jpeg;base64,{img_base64}"
#         return img_link
#     else:
#         return None

def add_movie(index,poster_link, movie_title, released_year, runtime, genre, rating, overview, director, stars, copies_available, price, movies_file):
    poster_link = "/Users/dam157/Downloads/" + poster_link
    print(poster_link)
    with open(movies_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([index,poster_link, movie_title, released_year, runtime, genre, int(rating), overview, director, stars, int(copies_available), int(price)])

def main():
    
    st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    
    st.title("Add New Movie")

    poster_image = st.file_uploader("Upload Movie Poster", type=['png', 'jpg', 'jpeg'])
    if poster_image:
        pp = poster_image.name
    
    movie_title = st.text_input("Movie Title")
    released_year = st.text_input("Released Year")
    runtime = st.number_input("Runtime", min_value=0)
    genre = st.text_input("Genre")
    rating = st.number_input("Rating", min_value=0, max_value=10)
    overview = st.text_input("Overview")
    director = st.text_input("Director")
    stars = st.text_input("Stars")
    copies_available = st.number_input("Copies Available", min_value=0)
    price = st.number_input("Price", min_value=0.0)

    if st.button("Add Movie"):
        movies_file = "movies_cleaned_dataset.csv"
        index = len(movies_file)+1
        
        # if check_movie_exists(movie_title, movies_file):
        #     st.error("Movie already exists!")
        # else:
            # poster_link = convert_image_to_link(poster_image)
        add_movie(index,pp, movie_title, released_year, runtime, genre, rating, overview, director, stars, copies_available, price, movies_file)
        st.success("Movie added successfully!")

if __name__ == "__main__":
    main()
