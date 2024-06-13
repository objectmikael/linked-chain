#####################################
# Employer/Validator Functionality
#####################################

# Import dependencies
import streamlit as st
from menu import menu_with_redirect
from functions import approve_request

# Redirects to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verifies the user's role
if st.session_state.role not in ["company-admin", "linkedchain-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.toast(f"You are currently logged in as an {st.session_state.role}.")

st.title("LinkedCHAIN")
st.header("",divider='rainbow')

st.header("Pending Validation Requests")
if "pending_validations" in st.session_state:
    for request in st.session_state.pending_validations:
        request_id = request["request_id"]
        user_address = request["user_address"]
        start_date = request["start_date"]
        end_date = request["end_date"]
        title = request["title"]
        responsibility = request["responsibility"]
        company_name = request["company_name"]
        company_address = request["approver_address"]
        
        st.write(f"Request ID: {request_id}")
        
        if st.button("Review Record"):
            st.write(f"User Address: {user_address}")
            st.write(f"Request ID: {request_id}")
            st.write(f"Company Name: {company_name}")
            st.write(f"Start Date: {start_date} End Date: {end_date}")
            st.write(f"Title: {title}")
            st.write(f"Responsibility: {responsibility}")

        if st.button(f":green[Validate Record]"):
            approve_request(company_address, request_id)  