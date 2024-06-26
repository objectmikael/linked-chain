#####################################
# Job Seeker Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import menu_with_redirect
from app import options_mapping, display_names
from functions import make_a_request

# Redirects to app.py if not logged in, otherwise show the navigation menu.
menu_with_redirect()

# Displays a toast notification indicating the user's current role
st.toast(f"You are currently logged in as a {st.session_state.role}.")

# Sets the page title and header with a rainbow divider.
st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Displays the header for submitting a validation request.
st.header("Submit a Request for Validation")

# Form for submitting a validation request.
user_name = st.selectbox("Select your address:", options=display_names)
user_address = options_mapping[user_name]

# Text inputs for the request details.
company_name = st.text_input("Company Name:")
start_date = st.text_input("Start Date:")
end_date = st.text_input("End Date:")
title = st.text_input("Title:")
responsibility = st.text_input("Responsibility:")

# Select box for choosing the company's address for approval.
company_name = st.selectbox("Select the company address for approval:", options=display_names)
company_address = options_mapping[company_name]

# Submit Request button.
if st.button(":green[Submit Request]"):
    make_a_request(user_address, company_name, start_date, end_date, title, responsibility, company_address)
