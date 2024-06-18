
import streamlit as st

st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬', initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
st.title("Welcome To Alpha Movies")

def details(name, surname, cellphone, email, address, password):
    with open('Client_Details.csv', 'a') as file:
        file.write(f"\n{name},{surname},{cellphone},{email},{address},{password}")

def mail(email):
    if "@" in email:
        return True
    else:
        return False

def phone(cellphone):
    if len(cellphone) > 0 and cellphone[0] == '0':
        return True
    else:
        return False

def main():
    
    st.write("Sign up now")

    name = st.text_input("Enter your Name")
    surname = st.text_input("Enter your Surname")
    cellphone = st.text_input("Enter your cellphone number", max_chars=10)
    email = st.text_input("Enter your email")
        
    address = st.text_input("Enter your Address")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up Now"):
        if password == confirm_password:
            if mail(email) and phone(cellphone):
                details(name, surname, cellphone, email, address, password)
                st.success("Sign up successful! Your details have been saved.")
                st.page_link("client_signin.py", label = "Go to Sign in page")
            else:
                st.error("Please enter valid cellphone number starting with '0' and/or a valid email address") 
        else:
            st.error("Passwords do not match. Please re-enter.")



if __name__ == "__main__":
    main()
