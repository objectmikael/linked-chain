#####################################
# Token Distribution Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import menu_with_redirect
from app import w3
from functions import transfer_tokens
from app import options_mapping, display_names

# Redirects to app.py if not logged in, otherwise show the navigation menu.
menu_with_redirect()

# Verifies the user's role
if st.session_state.role not in ["linkedchain-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

# Displays a toast notification indicating the user's current role.
st.toast(f"You are currently logged in as a {st.session_state.role} at LinkedCHAIN.")

# Sets the page title and header with a rainbow divider.
st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Displays the header for token transfer functionality.
st.header("Token Transfer")

# Gets the list of Ethereum accounts.
accounts = w3.eth.accounts

# Form for token transfer.
# Text input for the sender's name, default is "LinkedCHAIN".
sender_name = st.text_input("Sender address:", "LinkedCHAIN")
sender_address = options_mapping[sender_name]

# Number input for the amount of tokens to transfer.
amount = st.number_input("Number of tokens to transfer:", 1)

# Select box for choosing the receiver's address.
receiver_name = st.selectbox("Select receiver address:", options=display_names)
receiver_address = options_mapping[receiver_name]

# Transfer Tokens button.
if st.button(":green[Transfer Tokens]"):
    transfer_tokens(sender_address, receiver_address, amount)