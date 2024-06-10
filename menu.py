#####################################
# Menu-related functions.
#####################################

# Imports Dependencies.
import streamlit as st

# Defines a function for a navigation menu for authenticated users.
def authenticated_menu():
    st.sidebar.page_link("app.py", label="Switch accounts")
    if st.session_state.role == "user":
        st.sidebar.page_link("pages/user.py", label="Make Requests")
    elif st.session_state.role == "company-admin":
        st.sidebar.page_link("pages/company-admin.py", label="Validate Requests")
        st.sidebar.page_link("pages/query.py", label="Find Your Fit")
    elif st.session_state.role == "linkedchain-admin":
        st.sidebar.page_link("pages/linkedchain-admin.py", label="Transfer Tokens")

# Defines a function for a navigation menu for unauthenticated users.
def unauthenticated_menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/about-us.py", label="About Us")
    st.sidebar.page_link("pages/crowdsale.py", label="Crowdsale")

# Defines a function to determine if a user is logged in or not,
# then show the correct navigation menu.
def menu():
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()

# Defines a function to redirect users to the main page if not logged in,
# otherwise continue to render the navigation menu.
def menu_with_redirect():
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
