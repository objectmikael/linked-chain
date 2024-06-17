#####################################
# Employer/Validator Functionality
#####################################

# Import dependencies
import streamlit as st
from menu import menu_with_redirect
from functions import approve_request

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

# Displays the header for pending validation requests.
st.header("Pending Validation Requests")

# Checks if there are any pending validation requests in session state.
if "pending_validations" in st.session_state:
    # Initializes a dictionary to store requests by company.
    company_requests = {}

    # Organizes requests by company name.
    for request in st.session_state.pending_validations:
        company_name = request["company_name"]
        if company_name not in company_requests:
            company_requests[company_name] = []
        company_requests[company_name].append(request)
    
    # Displays the requests grouped by company name.
    for company_name, requests in company_requests.items():
        if requests:
            st.subheader(f"{company_name}")
            for request in requests:
                # Extracts request details.
                request_id = request["request_id"]
                user_address = request["user_address"]
                start_date = request["start_date"]
                end_date = request["end_date"]
                title = request["title"]
                responsibility = request["responsibility"]
                company_name = request["company_name"]
                company_address = request["approver_address"]
                
                # Displays the request summary.
                st.write("**New Request:**")
                
                # Creates a button to review the request details.
                if st.button(f"Review Record - {request_id}"):
                    st.markdown(f"""
                        Request ID: {request_id}  &nbsp;&nbsp;&nbsp; User Address: {user_address} \n
                        **{company_name}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**{start_date}** - **{end_date}** \n
                        **{title}** \n
                         &nbsp;&nbsp;&nbsp;- {responsibility}

                    """, unsafe_allow_html=True)

                # Creates a button to validate the request.
                if st.button(f":green[Validate Record - {request_id}]"):
                    approve_request(company_address, request_id)