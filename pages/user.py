#####################################
# Job Seeker Functionality
#####################################

# Imports dependencies.
import streamlit as st
from utility.menu import menu_with_redirect

# Redirects to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.toast(f"You are currently logged in as a {st.session_state.role}.")

st.title(":green[LinkedCHAIN]")
st.header("",divider='rainbow')

st.header("Submit a Request for Validation")