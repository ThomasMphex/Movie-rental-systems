import streamlit as st
from datetime import datetime
import pandas as pd
import csv

# Load data
movies_orders = pd.read_csv('movies_cleaned_dataset.csv')

# Function to retrieve total price from CSV
def get_total_price():
    try:
        with open('temporary_price.csv', 'r') as file:
            reader = csv.reader(file)
            total_pay = float(next(reader)[0])
            return total_pay
    except FileNotFoundError:
        return 0.0

# Define bank names
bank_names = ["Absa bank", "Capitec bank", "FNB", "Nedbank", "TymeBank", "Standard bank"]

# Function to get branch code
def get_branch_code(bank_name):
    bank_data = {
        "Capitec bank": "470010",
        "FNB": " 250655",
        "TymeBank": "678910",
        "Absa bank":"632005",
        "Nedbank":" 198765",
        "Standard bank":"051001"
    }
    return bank_data.get(bank_name, "Branch code not found")

def validate_payment(card_number, cvv):
    if len(card_number) != 16 or not card_number.isdigit():
        return False
    if len(cvv) != 3 or not cvv.isdigit():
        return False
    return True

# streamlit UI
def main():
    
    st.title("Banking Details")
    
    # Input fields for bank name, month, and year
    bank_name = st.selectbox("Bank Name", bank_names)
    branch_code = get_branch_code(bank_name)
    if st.button("Branch code", key="btt1"):
        if branch_code:
            st.success(f"Branch Code for {bank_name}: {branch_code}")
        else:
            st.error(f"No branch code found for {bank_name}")

    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    expiring_month = st.selectbox("Select Expiry Month", options=list(range(1, 13)), index=current_month - 1)
    expiring_year = st.selectbox("Select Expiry Year", options=list(range(current_year, current_year + 10)), index=0)

    selected_date = datetime(expiring_year, expiring_month, 1)
    if selected_date < current_date:
        st.warning("Card has already expired. Please select an unexpired expiration date.")
    else:
        st.success("Card expiration date is valid!")

        st.write(f"Expiring Month: {expiring_month}")
        st.write(f"Expiring Year: {expiring_year}")

    # Payment validation and processing
    card_number = st.text_input('Enter Card Number (16 digits):', max_chars=16)
    cvv = st.text_input('Enter CVV (3 digits):', max_chars=3)

    movie_data = pd.read_csv('movies_cleaned_dataset.csv')

   
    total_pay = get_total_price()  # Initialize total_pay to keep track of the total amount

    

    st.write(f'Total Amount: R{total_pay}')

    # Pay button
    if st.button('Pay', key="btt2"):
        if total_pay > 0:
            st.write(f'Total Amount to Pay: R{total_pay}')
            if validate_payment(card_number, cvv):
                st.success('Payment successful! please bring your ID FOR COLLECTION within 2 Days & movie will be collected after 8 Days')
                # Save updated movie data to CSV after successful payment
                movie_data.to_csv('movies_cleaned_dataset_updated.csv', index=False)
            else:
                st.error('Invalid input! Please enter a 16-digit Account Number and a 3-digit CVV.')
        else:
            st.write('No movies selected or copies to rent!')

    st.page_link("pages/home.py", label="HOME")

if __name__ == '__main__':
    main()
