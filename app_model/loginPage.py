import streamlit as st
import functions

### Session states assignments
if "isUserLoggedIn" not in st.session_state:
    st.session_state.isUserLoggedIn = False
if "username" not in st.session_state:
    st.session_state.username = ""
###

### Prevent the user from re-logging in
if st.session_state.isUserLoggedIn:
    st.success("You are already logged in")
###
else:
    st.set_page_config(page_title="Login Page")
    st.title("Login Page")
    with st.form("Login"):
        ### Inputs
        username = st.text_input("Enter your username: ", placeholder="Username")
        password = st.text_input("Enter your password: ", placeholder="Password", type="password")
        ###
        if st.form_submit_button("Sign In", key="signInButton"):
            ### Checks
            if username == "" or password == "":
                st.warning("Please enter both username and password")
            ###
            else:
               if functions.loginUser(username, password): # If true, proceed to set username and isLoggedIn
                   st.session_state.username = username
                   st.session_state.isUserLoggedIn = True
                   st.switch_page("app_model/homePage.py")

    if st.button("Not registered yet? Click here to sign up", key="signUpButton"):
        st.switch_page('app_model/signUpPage.py')


    st.html("""
    <style>
    @keyframes hoverEffect {
        from { background-color: black; }
        to { background-color: white; color:black}
    }
    .st-key-signUpButton:hover button { animation: hoverEffect 0.4s ease-in-out forwards;}   
    .st-key-signInButton:hover button {animation: hoverEffect 0.4s ease-in-out forwards;}
    </style>
    """)