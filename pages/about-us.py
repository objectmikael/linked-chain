#####################################
# LinkedCHAIN Description
#####################################

# Imports dependencies
import streamlit as st
from menu import unauthenticated_menu

# Shows the navigation menu for unauthenticated users
unauthenticated_menu()

st.title("LinkedCHAIN")
st.header("",divider='rainbow')

# Mission Section
st.subheader("Mission")
st.write("To revolutionize the job application and verification process by leveraging blockchain technology, "
         "creating a secure, transparent, and efficient system that empowers both job seekers and employers.")

# Vision Section
st.subheader("Vision")
st.write("To become the global standard for professional history management, where trust, efficiency, and authenticity "
         "in job verification are guaranteed, ensuring a seamless hiring experience for all stakeholders.")

# Principles Section
st.subheader("Principles")
principles = [
    "Transparency: Ensuring complete transparency in the job application process, making all professional histories easily verifiable and accurate.",
    "Security: Prioritizing security by using blockchain technology to protect all data against unauthorized access.",
    "Efficiency: Streamlining the job application process to reduce time and effort for both job seekers and employers.",
    "User-Centric Design: Focusing on intuitive and accessible design to ensure all users can easily navigate and benefit from our platform."
]
for principle in principles:
    st.write(f"**{principle.split(': ')[0]}**")
    st.write(principle.split(': ')[1])

# Values Section
st.subheader("Values")
values = [
    "Trust: Building a trustworthy environment where all participants can rely on the authenticity of job histories.",
    "Innovation: Committing to continuous innovation by using the latest blockchain and UI technologies to enhance our platform.",
    "Integrity: Upholding the highest standards of integrity in all operations, ensuring honesty and fairness.",
    "Collaboration: Believing in the power of collaboration, working closely with companies, academic institutions, and job seekers to create a beneficial system for everyone.",
    "Sustainability: Adopting a sustainable approach to create long-term value for all stakeholders in the employment verification process."
]
for value in values:
    st.write(f"**{value.split(': ')[0]}**")
    st.write(value.split(': ')[1])