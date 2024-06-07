#####################################
# Token Distribution Functionality
#####################################

# Imports dependencies
import streamlit as st
from utility.menu import menu_with_redirect

# Redirects to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verifies the user's role
if st.session_state.role not in ["super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.toast(f"You are currently logged in as a {st.session_state.role} at LinkedCHAIN.")

st.title(":green[LinkedCHAIN]")
st.header("",divider='rainbow')

st.header("Token Transfer")