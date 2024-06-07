#####################################
# Main Python script for
# running the application.
#####################################

# Imports Dependencies
import os
from web3 import Web3
import streamlit as st
from dotenv import load_dotenv
from utility.menu import menu

# Loads env variables.
load_dotenv()

# Connects to Ganache.
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Checks connection to Ganache.
if w3.isConnected():
    st.success("Connected to Ethereum via Ganache")
else:
    st.error("Failed to connect to Ethereum")

# Initializes st.session_state.role to None.
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieves the role from session state to initialize the widget
st.session_state._role = st.session_state.role
def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role

# Creates selectbox to choose role.
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role
)

# Renders the dynamic menu!
menu() 

st.markdown(""" 
    <center>
        <h1 style='color:orange;'>
            Welcome to 
                <span style='color:green; text-decoration: underline; text-decoration-color: black;'>
                    LinkedCHAIN
                </span>
        </h1>
        <h5>A Blockchain Professional History Management Tool</h5>
    </center>""", unsafe_allow_html=True)

st.header("",divider='rainbow')