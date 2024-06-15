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
    company_requests = {}
    for request in st.session_state.pending_validations:
        company_name = request["company_name"]
        if company_name not in company_requests:
            company_requests[company_name] = []
        company_requests[company_name].append(request)
    
    for company_name, requests in company_requests.items():
        if requests:
            st.subheader(f"{company_name}")
            for request in requests:
                request_id = request["request_id"]
                user_address = request["user_address"]
                start_date = request["start_date"]
                end_date = request["end_date"]
                title = request["title"]
                responsibility = request["responsibility"]
                company_name = request["company_name"]
                company_address = request["approver_address"]
                
                st.write(f"**New Request:**")
                
                if st.button(f"Review Record - {request_id}"):
                    st.markdown(f"""
                        Request ID: {request_id}  &nbsp;&nbsp;&nbsp; User Address: {user_address} \n
                        **{company_name}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**{start_date}** - **{end_date}** \n
                        **{title}** \n
                         &nbsp;&nbsp;&nbsp;- {responsibility}

                    """, unsafe_allow_html=True)

                if st.button(f":green[Validate Record - {request_id}]"):
                    approve_request(company_address, request_id)  