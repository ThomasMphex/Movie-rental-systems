import streamlit as st

def save_details( username,employee_number,email_address, password):
    with open('Employee_Details.csv', 'a') as file:
        file.write(f"\n{username},{employee_number},{email_address},{password}")

def validate_email(email):
    if "@" in email:
        return True
    else:
        return False


def main():
    
    st.set_page_config(layout='centered', page_title='Alpha Movies', page_icon='🎬')
    st.markdown("<h1 style='text-align: center; color: red; font-size: 32px;'>🎬 Alpha Movies</h1>", unsafe_allow_html=True)
    
    st.title("Admin Sign Up")

    
    username = st.text_input("Enter new Username")
    employee_number = st.text_input("Enter new Employee Number")
    email_address = st.text_input("Enter email address")
    password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up Now"):
        if password == confirm_password:
            if validate_email(email_address):
                save_details(username,employee_number,email_address, password)
                st.success("Sign up successful! Your details have been saved.")
                st.page_link("pages/admin_signin.py", label = "proceed")
            else:
                st.error("Please enter a valid email address")
        else:
            st.error("Passwords do not match. Please re-enter.")

if __name__ == "__main__":
    main()
