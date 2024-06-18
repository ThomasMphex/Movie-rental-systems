import streamlit as st
import csv
import smtplib
from email.message import EmailMessage
import random

def read_csv(file_path):
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            records.append(row)
    return records

def find_user_by_username(username, records):
    for record in records:
        if record[0] == username:
            return record
    return None

def send_email_with_link(email, link):
    msg = EmailMessage()
    msg.set_content(f"Click the following link to reset your password: {link}")
    msg['Subject'] = "Reset Password Link"
    msg['From'] = "Thomas.Mpherwane8@gmail.com"  # Update with your email
    msg['To'] = email

    with smtplib.SMTP("smtp.elasticemail.com", 2525) as server:  # Update with your SMTP server details
        server.starttls()
        server.login("Thomas.Mpherwane8@gmail.com", "D7A2A65B01090895CB5A66E4C3F152A4D3C2")  # Update with your email credentials
        server.send_message(msg)

def generate_pin():
    return ''.join(random.choices('0123456789', k=6))

def main():
    st.title("Forgot Login Details")

    username = st.text_input("Enter Username")

    if st.button("Reset Password"):
        records = read_csv("Employee_Details.csv")
        user = find_user_by_username(username, records)
        if user:
            email = user[2]  # Assuming email is in the 4th column
            pin = generate_pin()
            link = f"http://localhost:8541/forgot_password?pin={pin}"  # Update with your website URL
            send_email_with_link(email, link)
            st.success("Password reset link sent to your email.")
        else:
            st.error("Username not found. Please try again.")

    st.title("Validate Information")

    pin_input = st.text_input("Enter Pin from Email")
    top_pin = "123456"  # Top pin to validate

    if st.button("Validate"):
        if pin_input == top_pin:
            st.success("Validation successful.")
        else:
            st.error("Invalid pin. Please try again.")

if __name__ == "__main__":
    main()
