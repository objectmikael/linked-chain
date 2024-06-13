#####################################
# LinkedCHAIN Product Roadmao
#####################################

# Imports dependencies.
import streamlit as st
from menu import unauthenticated_menu

# Shows the navigation menu for unauthenticated users.
unauthenticated_menu()

st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Token Description
st.subheader("Product Roadmap")
st.write("We are excited to share the future direction of our platform. Our goal is to enhance functionality, security, and user experience while reducing costs. Below are the key improvements we are working on:")

# Roadmap item 1: Reduce Transaction Costs
st.subheader("1. Reduce Transaction Costs")
st.write("To minimize transaction fees, we are exploring alternatives to the Ethereum blockchain. Platforms such as Solana and Polygon are being considered for their lower costs and high efficiency. This transition will enable us to offer a more cost-effective service for all users.")

# Roadmap item 2: Enhance Security and Access Control
st.subheader("2. Enhance Security and Access Control")
st.write("Security is our top priority. We will implement comprehensive security measures and access controls tailored to different user roles, including investors, admins, companies, and core users. This will ensure that all user data is protected and that only authorized individuals have access to sensitive information.")

# Roadmap item 3: Expand Functionalities
st.subheader("3. Expand Functionalities")
st.write("We plan to develop robust functionalities that will allow users to make requests, enable companies to validate those requests, and provide the capability for anyone within the ecosystem to query the blockchain. These enhancements will streamline processes and improve transparency and efficiency.")

# Roadmap item 4: Improve User Interface
st.subheader("4. Improve User Interface")
st.write("To deliver a superior user experience, we are moving away from Streamlit and adopting more versatile frameworks such as React. This change will result in a more responsive, intuitive, and visually appealing interface for our users.")

# Closing remarks
st.markdown("We are committed to continuous improvement and will keep our community informed as we make progress on these initiatives. Thank you for being a part of our journey!")