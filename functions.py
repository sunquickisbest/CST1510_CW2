import streamlit as st
import bcrypt as b

def passwordChecker(x):
    with open('pages/textFiles/users.txt', 'r') as file:
        for i in file:
            username, password = i.strip().split(',')
            if b.checkpw(x.encode('utf-8'), password.encode('utf-8')):
                print("Correct password!")
                return True
        return False

def usernameChecker(x):
    with open('pages/textFiles/users.txt', 'r') as file:
        for i in file:
            username, password = i.strip().split(',')
            if username == x:
                return True
        return False

def registerUser(x, y):
    with open('pages/textFiles/users.txt', 'a') as file:
        file.seek(0)
        if usernameChecker(x):
            st.warning("Username already taken!")
            return False
        else:
            encodedPassword = y.encode('utf-8')
            hashedPassword = b.hashpw(encodedPassword, b.gensalt()).decode('utf-8')
            file.write(f"{x},{hashedPassword}\n")
            st.success("User registered successfully!")
            with open('pages/textFiles/userImages.txt', 'a') as f:
                f.write(f"{x},defaultProfile.jpg\n")
            return True

def loginUser(x, y):
    if not usernameChecker(x):
        st.warning("Username was not found, please check again or sign up")
        return False
    else:
        if passwordChecker(y):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Incorrect password, please try again!")
            return False