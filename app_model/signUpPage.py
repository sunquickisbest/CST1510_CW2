import streamlit as st
import functions

st.set_page_config(page_title="Sign-up Page")

st.title("Sign-up Page")
with st.form("Sign Up"):
        username = st.text_input("Enter a username: ", placeholder="Username")
        password = st.text_input("Enter a password: ", placeholder="Password", type="password")
        lengthCheck, symbolCheck, notContainUsernameCheck = False, False, False
        if st.form_submit_button("Sign up", key="signUpButton"):
            if username == "" or password == "":
                    st.warning("Please both enter a username and password")
            elif not username.isalnum():
                    st.warning("Username cannot contain symbols!")
            else:
                if len(password) < 8:
                    st.write(":red[Password must be at least 8 characters]")
                else:
                    lengthCheck = True

                if password.isalnum():
                    st.write(":red[Password must contain at least 1 symbol]")
                else:
                    symbolCheck = True

                if not password.find(username):
                    st.write(":red[Password CANNOT contain your username]")
                else:
                    notContainUsernameCheck = True

                if lengthCheck and symbolCheck and notContainUsernameCheck:
                    functions.registerUser(username, password)



if st.button("Already have an account? Click here to sign in", key="signInButton"):
        st.switch_page("app_model/loginPage.py")

st.html("""
        <style>
        @keyframes hoverEffect {
            from {
                background-color: black;
            }
            to {
                background-color: white;
                color:black
            }
        }
        
        .st-key-signUpButton:hover button {
            animation: hoverEffect 0.4s ease-in-out forwards;
        }
        
        .st-key-signInButton:hover button {
            animation: hoverEffect 0.4s ease-in-out forwards;
        }
        </style>
        """)