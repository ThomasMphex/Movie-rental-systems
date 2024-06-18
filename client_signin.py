import streamlit as st
import csv


st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬', initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
st.title(" Alpha Movies")

#Import csv file

def read_csv(file_path):
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            records.append(row)
    return records

def details(email, password, records):
    for record in records:
        if record[3] == email and record[5] == password:
            return True
    return False


def main():
    st.title(" Sign In")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign In"):
        records = read_csv("Client_Details.csv")
        if details(email, password, records):
             st.page_link("pages/home.py", label = "proceed")
           
        else:
            st.error("Incorrect credentials. Please try again.") 
    
    
    #if st.button ("Create Account"):
    st.page_link("pages/client_signup.py", label = "Create Account")
        
        
if __name__ == "__main__":
    main()

