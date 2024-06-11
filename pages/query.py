#####################################
# Record Querying Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import menu_with_redirect

# Redirects to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verifies the user's role
if st.session_state.role not in ["company-admin", "linkedchain-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.toast(f"You are currently logged in as an {st.session_state.role}.")

st.title(":green[LinkedCHAIN]")
st.header("",divider='rainbow')

st.header("Query the Blockchain to Find a Match ")