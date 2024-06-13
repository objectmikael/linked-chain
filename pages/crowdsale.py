#####################################
# Crowdsale Functionality
#####################################

# Imports dependencies.
import streamlit as st
from menu import unauthenticated_menu
from app import options_mapping, display_names
from functions import purchase_tokens

# Shows the navigation menu for unauthenticated users.
unauthenticated_menu()

st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Token Description
st.subheader("What is Hyrd (HYD) Token?")
st.write("Hyrd (HYD) is an ERC20 token used within the LinkedCHAIN ecosystem. It facilitates the validation and endorsement of job histories by allowing companies to participate in the validation process.")

# How the Crowdsale Works
st.subheader("How Does the Crowdsale Work?")
st.write("""
The crowdsale allows companies to purchase Hyrd (HYD) tokens, which they can then use to validate and endorse job histories. Here’s how it works:

1. **Purchasing HYD Tokens**: Participants can purchase HYD tokens at a rate of 1 HYD per unit cost, with a minimum purchase of 100 tokens. These tokens are stored in a distribution wallet managed by LinkedCHAIN.
2. **Becoming an Admin**: Entities that complete a transaction via the crowdsale are marked as admins within the ecosystem.
3. **Token Distribution**: The distribution wallet can disperse HYD tokens to individual wallets/users upon request.
4. **Validation Requests**: Users with HYD tokens can request validation of their employment records from an admin wallet(company).
5. **Admin Validation**: Admins can accept or decline validation requests. Accepted requests are queryable on the blockchain, ensuring the authenticity of job histories.

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
st.write("Participating in the LinkedCHAIN crowdsale provides several benefits:")
for benefit in benefits:
    st.write(f"- {benefit}")

# Final Note
st.write("Join the LinkedCHAIN ecosystem today and help us revolutionize the job application and verification process!")

st.divider()
purchaser_name = st.selectbox("Select Purchaser Address:", options=display_names)
purchaser_address = options_mapping[purchaser_name]
purchase_amount = st.number_input("Enter the amount of tokens to purchase (1token = 0.5ETH):", min_value=100)
beneficiary_name = st.text_input("Beneficiary:", "LinkedCHAIN")
beneficiary_address = options_mapping[beneficiary_name]

if st.button(":green[Purchase Tokens]"):
    purchase_tokens(purchaser_address, beneficiary_address, purchase_amount)
    
