import pandas as pd
import streamlit as st
import csv
import os

def delete_movie(movie_title, movies_file):
    temp_file = "temp.csv"  # Temporary file to store non-deleted movies
    with open(movies_file, 'r', newline='') as file, open(temp_file, 'w', newline='') as temp:
        reader = csv.reader(file)
        writer = csv.writer(temp)
        deleted = False
        for row in reader:
            if row[2] == movie_title:
                deleted = True
            else:
                writer.writerow(row)
    if deleted:
        # Replace the original file with the temporary file
        os.remove(movies_file)
        os.rename(temp_file, movies_file)
        return True
    return False

def main():
    st.set_page_config(layout='wide', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    st.title("Alpha Movies")

    # Load data
    movie_df = pd.read_csv('movies_cleaned_dataset.csv')

    # Convert 'Released_Year' column to integers where possible
    movie_df['Released_Year'] = pd.to_numeric(movie_df['Released_Year'], errors='coerce')

    # Sidebar with search options
    st.sidebar.title("Welcome to Alpha Movies")
    search_type = st.sidebar.selectbox("Search by:", ["Title", "Genre", "Released Year"])
    search_query = st.sidebar.text_input("Enter your search query:")

    # List of all genres
    all_genres = sorted(set(','.join(movie_df['Genre']).split(',')))
    all_genres.insert(0, "")  # Insert empty string as the first option
    genre_option = st.sidebar.selectbox("Select Genre:", all_genres)

    # Filter movies based on search query and genre
    if search_query:
        if search_type == "Title":
            filtered_movies = movie_df[movie_df['Movies'].str.contains(search_query, case=False)]
        elif search_type == "Released Year":
            try:
                search_year = int(search_query)
                filtered_movies = movie_df[movie_df['Released_Year'] == search_year]
            except ValueError:
                st.error("Please enter a valid year.")
                return
        else:  # Search by Genre
            if genre_option:
                filtered_movies = movie_df[movie_df['Genre'].str.contains(genre_option, case=False)]
            else:
                filtered_movies = movie_df
    else:
        if genre_option:
            filtered_movies = movie_df[movie_df['Genre'].str.contains(genre_option, case=False)]
        else:
            filtered_movies = movie_df

    # Display filtered movies
    if filtered_movies.empty:
        st.subheader("No results found.")
    else:
        num_cols = 4
        num_movies = len(filtered_movies)
        num_rows = (num_movies + num_cols - 1) // num_cols

        cols = st.columns(num_cols)
        for idx, movie in filtered_movies.iterrows():
            row = idx // num_cols
            col = idx % num_cols
            with cols[col]:
                st.subheader(movie['Movies'])
                st.image(movie['Poster_Link'], width=150)

                # Deletion button with confirmation box
                delete_flag_key = f"delete_flag_{idx}"
                delete_flag = st.checkbox("🗑️ Delete Movie", key=delete_flag_key)
                if delete_flag:
                    confirmation_key = f"confirmation_{idx}"
                    confirmation = st.checkbox("🗑️ Are you sure you want to delete this movie?", key=confirmation_key)
                    if confirmation:
                        if delete_movie(movie['Movies'], 'movies_cleaned_dataset.csv'):
                            st.success(f"Movie '{movie['Movies']}' deleted successfully! Reload page to see results")
                        else:
                            st.error(f"Failed to delete movie '{movie['Movies']}'.")

if __name__ == "__main__":
    main()

















