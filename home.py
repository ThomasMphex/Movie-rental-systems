import streamlit as st
import pandas as pd
import csv  # Add import statement for CSV
from datetime import datetime

# Load data
movie_data = pd.read_csv('movies_cleaned_dataset.csv')

# Initialize cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

def validate_payment(card_number, cvv):
    if len(card_number) != 16 or not card_number.isdigit():
        return False
    if len(cvv) != 3 or not cvv.isdigit():
        return False
    return True

def add_to_cart(movie_details):
    # Add movie to cart
    st.session_state.cart.append(movie_details)
    st.success("Added to Cart")

def save_price(total_pay):
    # Save total price to CSV file
    with open('temporary_price.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([total_pay])

def main():
    st.title("Alpha Movies")

    # Sidebar with search options
    st.sidebar.title("Welcome to Alpha Movies")
    Movies = st.sidebar.text_input("Enter Movie Title:")
    Released_Year = st.sidebar.text_input("Enter Released Year:")
    Genre = st.sidebar.selectbox("Select Genre:", [""] + list(movie_data['Genre'].unique()))

    search_button = st.sidebar.button("Search")
    
    # Cart button and payment form
    if st.button("View Cart", key="button1"):
        if st.session_state.cart:
            st.header("Your Cart:")
            for item in st.session_state.cart:
                st.write(f"Movie: {item['Movies']}")
                st.write(f"Price: {item['Prices']}")
            total_pay = sum(item['Prices'] for item in st.session_state.cart)
            save_price(total_pay)  # Save total price to CSV file
            st.write(f'Total Amount: R{total_pay}')
            st.page_link("pages/payment.py", label="Proceed to Payment")

    # Display movies
    num_cols = 4  # Number of columns in the grid
    num_movies = len(movie_data)
    num_rows = (num_movies + num_cols - 1) // num_cols  # Calculate number of rows

    # Create columns for the grid
    cols = st.columns(num_cols)

    # Display movie details in the grid
    idx = 0
    while idx < num_movies:
        for row in range(num_rows):
            for col in range(num_cols):
                if idx < num_movies:
                    if filter_movie(movie_data.iloc[idx], Movies, Released_Year, Genre):
                        with cols[col]:
                            # Movie poster and title
                            st.image(movie_data["Poster_Link"][idx], width=120)
                            st.markdown(f"<h3 style='font-size: 18px;'>{movie_data['Movies'][idx]}</h3>", unsafe_allow_html=True)
                            if st.button(f"Add to Cart", key=f"add_to_cart_{idx}"):  # Use unique key based on movie title and index
                                add_to_cart(movie_data.iloc[idx])  # Add movie to cart
                    idx += 1

    card_number = st.text_input('Enter Card Number (16 digits):', max_chars=16)
    cvv = st.text_input('Enter CVV (3 digits):', max_chars=3)

    # Pay button
    if st.button('Proceed to Payment', key="btt2"):
        if st.session_state.cart:
            total_pay = sum(item['Prices'] for item in st.session_state.cart)
            st.write(f'Total Amount to Pay: R{total_pay}')
            if validate_payment(card_number, cvv):
                st.success('Payment processed successfully!')
                # Clear the cart after successful payment
                st.session_state.cart = []
            else:
                st.error('Invalid input! Please enter a 16-digit Account Number and a 3-digit CVV.')
        else:
            st.write('No movies selected or copies to rent!')

def filter_movie(movie_details, title, year, genre):
    # Filter movie based on search criteria
    if title and title.lower() not in movie_details['Movies'].lower():
        return False
    if year and str(movie_details['Released_Year']) != year:
        return False
    if genre and genre != movie_details['Genre']:
        return False
    return True

if __name__ == "__main__":
    main()
