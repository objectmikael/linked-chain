#####################################
# Record Querying Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import menu_with_redirect
from app import options_mapping, display_names
from functions import query_approved_requests

# Redirects to app.py if not logged in, otherwise show the navigation menu.
menu_with_redirect()

# Verifies the user's role.
if st.session_state.role not in ["company-admin", "linkedchain-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

# Displays a toast notification indicating the user's current role.
st.toast(f"You are currently logged in as an {st.session_state.role}.")

# Sets the page title and header with a rainbow divider.
st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Displays the header for account lookup functionality.
st.header("Account Lookup")

# Select box for choosing the Ethereum account address.
account_name = st.selectbox("Select the Ethereum Account Address:", options=display_names)
account_address = options_mapping[account_name]

# Query Approved Requests button.
if st.button(':green[Query Approved Requests]'):
    approved_requests = query_approved_requests(account_address)
    if not approved_requests:
        st.error('No approved requests found for this account.')
    else:
        # Displays the approved requests.
        for request in approved_requests:
            st.markdown(f"""
                <h3> {request[1]} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {request[2]} - {request[3]}</h3>
                <h5> {request[4]} </h5>
                <text> &nbsp;&nbsp;&nbsp;+ {request[5]}</text>
                <br>
                <br>
            """, unsafe_allow_html=True)
