import streamlit as st
import functions

if "isUserLoggedIn" not in st.session_state:
    st.session_state.isUserLoggedIn = False
if "username" not in st.session_state:
    st.session_state.username = ""

st.set_page_config(page_title="Login Page")
st.title("Login Page")
with st.form("Login"):
    username = st.text_input("Enter your username: ", placeholder="Username")
    password = st.text_input("Enter your password: ", placeholder="Password", type="password")
    if st.form_submit_button("Sign In", key="signInButton"):
        if username == "" or password == "":
            st.warning("Please enter both username and password")
        else:
           if functions.loginUser(username, password):
               st.session_state.username = username
               st.session_state.isUserLoggedIn = True
               st.switch_page("pages/homePage.py")

if st.button("Not registered yet? Click here to sign up", key="signUpButton"):
    st.switch_page('main.py')


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