import streamlit as st

cyberIncidents = st.Page("app_model/Cyber_Incidents.py", visibility="hidden")
homePage = st.Page("app_model/homePage.py", title="Home Page", visibility="hidden")
loginPage = st.Page("app_model/loginPage.py", title="Login Page", visibility="hidden")
Metadata = st.Page("app_model/Metadata.py", title="Metadata Page", visibility="hidden")
itTickets = st.Page("app_model/IT_Tickets.py", title="IT Tickets", visibility="hidden")
profilePage = st.Page("app_model/profilePage.py", title="Profile Page", visibility="hidden")
signupPage = st.Page("app_model/signUpPage.py", title="Signup Page", visibility="hidden")
profileofUserChosen = st.Page("app_model/profileOfUserChosen.py", title="Profile Of User Chosen", visibility="hidden")

navigationPage = st.navigation([signupPage, loginPage, homePage, profilePage, cyberIncidents, Metadata, itTickets,profileofUserChosen], position="top")
navigationPage.run()
