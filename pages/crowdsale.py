#####################################
# Crowdsale Functionality
#####################################

# Imports dependencies.
import streamlit as st
from utility.menu import unauthenticated_menu

# Shows the navigation menu for unauthenticated users.
unauthenticated_menu()

st.title(":green[LinkedCHAIN]")
st.header("",divider='rainbow')

# Token Description
st.subheader("What is Hyrd (HYD) Token?")
st.write("Hyrd (HYD) is an ERC20 token used within the LinkedChain ecosystem. It facilitates the validation and endorsement of job histories by allowing companies to participate in the validation process.")

# How the Crowdsale Works
st.subheader("How Does the Crowdsale Work?")
st.write("""
The crowdsale allows companies to purchase Hyrd (HYD) tokens, which they can then use to validate and endorse job histories. Here’s how it works:

1. **Purchasing HYD Tokens**: Participants can purchase HYD tokens at a rate of 1 HYD per unit cost, with a minimum purchase of 100 tokens. These tokens are stored in a distribution wallet managed by LinkedCHAIN.
2. **Becoming an Admin**: Entities that complete a transaction via the crowdsale are marked as admins within the ecosystem.
3. **Token Distribution**: The distribution wallet can disperse HYD tokens to individual wallets/users upon request.
4. **Validation Requests**: Users with HYD tokens can request validation of their employment records from an admin wallet(company).
5. **Admin Validation**: Admins can accept or decline validation requests. Accepted requests are added to the blockchain, ensuring the authenticity of job histories.

This system ensures a secure, efficient, and transparent process for validating professional histories.
""")

# Summary of Crowdsale Benefits
st.subheader("Benefits of Participating in the Crowdsale")
benefits = [
    "Secure and Transparent Job History Validation",
    "Streamlined Job Application Process",
    "Trust and Efficiency in Hiring",
    "Becoming a Trusted Validator within the Ecosystem"
]
st.write("Participating in the LinkedChain crowdsale provides several benefits:")
for benefit in benefits:
    st.write(f"- {benefit}")

# Final Note
st.write("Join the LinkedChain ecosystem today and help us revolutionize the job application and verification process!")

st.divider()