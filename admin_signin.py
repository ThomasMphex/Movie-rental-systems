import streamlit as st
import csv

def read_csv(file_path):
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            records.append(row)
    return records

def validate_credentials(username, employee_number, email_address, password, records):
    for record in records:
        if record[0] == username and record[1] == employee_number and record[2] == email_address and record[3] == password:
            return True
    return False

def main():
    
    st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)

    
    st.title("Administrator Sign In")
    
    username = st.text_input("Username")
    employee_number = st.text_input("Employee Number")
    email_address = st.text_input("Email address")
    password = st.text_input("Password", type="password")
    
    records = read_csv("Employee_Details.csv")
    
    if validate_credentials(username, employee_number, email_address, password, records):
        st.success("Redirecting to the Main Page")
        st.page_link("pages/manage_inventories.py", label = "Sign In")

    else:
        st.error("Incorrect credentials. Please try again.")
        st.page_link("pages/forgot_password.py", label = "Forgot Pawword") 

    st.markdown("Create a New Employee account")
    st.page_link("pages/admin_signup.py", label = "Sign Up Now")
    

if __name__ == "__main__":
    main()
