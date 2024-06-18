import streamlit as st
import pandas as pd

def modify_csv_file(df, modifications):
    for index, modification in modifications.items():
        row_index, column_name, new_value = modification
        df.at[row_index, column_name] = new_value
    return df

def main():
    st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    st.title("Update Movie Details")

    # Load data from CSV file
    df = pd.read_csv('movies_cleaned_dataset.csv')

    # Search query input
    search_query = st.text_input("Search for a movie:")

    # Perform search and display search results
    if search_query:
        search_results = df[df.apply(lambda row: search_query.lower() in ' '.join(map(str, row)).lower(), axis=1)]
    else:
        search_results = df
    
    if not search_results.empty:
        st.subheader("Search Results:")
        for index, row in search_results.iterrows():
            movie_title = row['Movies']
            copies_available = row["Copies_available"]
            movie_price = row ["Prices"]
            st.image(row['Poster_Link'], caption=movie_title)
            st.write(f"Copies available in Store: {copies_available}")
            st.write(f"The Current price of the movie: {movie_price}")
            new_price = st.text_input(f"Price for {movie_title}", row['Prices'])
            new_copies = st.text_input(f"Copies available for {movie_title}", row['Copies_available'])
            update_button = st.button(f"Update {movie_title}")
            if update_button:
                modifications = {}
                if new_price != row['Prices']:
                    modifications[(index, 'Prices', new_price)] = (index, 'Prices', new_price)
                if new_copies != row['Copies_available']:
                    modifications[(index, 'Copies_available', new_copies)] = (index, 'Copies_available', new_copies)
                if modifications:
                    df = modify_csv_file(df, modifications)
                    df.to_csv('movies_cleaned_dataset.csv', index=False)
                    st.success(f"Changes for '{movie_title}' applied successfully!")
                    st.subheader("Updated CSV File:")
                    st.write(df)
    else:
        st.write("No movies found matching the search criteria.")

if __name__ == "__main__":
    main()


















