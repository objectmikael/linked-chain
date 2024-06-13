#####################################
# Record Querying Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import menu_with_redirect
from app import options_mapping, display_names, requestsContract
from functions import query_approved_requests

# Redirects to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verifies the user's role
if st.session_state.role not in ["company-admin", "linkedchain-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.toast(f"You are currently logged in as an {st.session_state.role}.")

st.title("LinkedCHAIN")
st.header("",divider='rainbow')

st.header("Account Lookup")

# Input for Ethereum account address
account_name = st.selectbox("Select the Ethereum Account Address:", options=display_names)
account_address = options_mapping[account_name]

if st.button(':green[Query Approved Requests]'):
    approved_requests = query_approved_requests(account_address)
    # if not approved_requests:
    #     st.info('No approved requests found for this account.')
    # else:
    #     st.write('Approved Requests:')
    #     for request in approved_requests:
    #         st.write(f"ID: {request[0]}")
    #         st.write(f"Company Name: {request[1]}")
    #         st.write(f"Start Date: {request[2]}")
    #         st.write(f"End Date: {request[3]}")
    #         st.write(f"Title: {request[4]}")
    #         st.write(f"Responsibility: {request[5]}")
    #         st.write(f"Approver: {request[6]}")
    #         st.write('---')
    st.write(approved_requests)
