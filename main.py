import streamlit as st

cyberIncidents = st.Page("pages/Cyber_Incidents.py")
homePage = st.Page("pages/homePage.py", title="Home Page", visibility="hidden")
loginPage = st.Page("pages/loginPage.py", title="Login Page", visibility="hidden")
Metadata = st.Page("pages/Metadata.py", title="Metadata Page", visibility="hidden")
itTickets = st.Page("pages/IT_Tickets.py", title="IT Tickets", visibility="hidden")
profilePage = st.Page("pages/profilePage.py", title="Profile Page", visibility="hidden")
signupPage = st.Page("pages/signUpPage.py", title="Signup Page", visibility="hidden")
profileofUserChosen = st.Page("pages/profileOfUserChosen.py", title="Profile Of User Chosen", visibility="hidden")

navigationPage = st.navigation([signupPage, loginPage, homePage, profilePage, cyberIncidents, Metadata, itTickets,profileofUserChosen], position="top")
navigationPage.run()
