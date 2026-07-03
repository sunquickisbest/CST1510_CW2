import streamlit as st
import bcrypt as b
import sqlite3 as sql

def passwordCheckerForTxt(x):
    with open('pages/textFiles/users.txt', 'r') as file:
        for i in file:
            username, password = i.strip().split(',')
            if b.checkpw(x.encode('utf-8'), password.encode('utf-8')):
                print("Correct password!")
                return True
        return False

def passwordChecker(x, username):
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT password FROM users WHERE username = ?""", (username,))
        passwordCheck = cursor.fetchone()
        if passwordCheck is not None and b.checkpw(x.encode('utf-8'), passwordCheck[0].encode('utf-8')):
            return True
        return False


def usernameCheckerForTxt(x):
    with open('pages/textFiles/users.txt', 'r') as file:
        for i in file:
            username, password = i.strip().split(',')
            if username == x:
                return True
        return False

def usernameChecker(x):
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT username FROM users WHERE username = ?""", (x,))
        username = cursor.fetchone()
        if username is not None and username[0] == x:
            return True
        return False


def registerUserForTxt(x, y):
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

def registerUser(x, y):
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL, profilePicturePath TEXT NOT NULL);""")
        connection.commit()
        if not usernameChecker(x):
            hashedPassword = b.hashpw(y.encode('utf-8'), b.gensalt()).decode('utf-8')
            cursor.execute("""INSERT INTO users(username, password, profilePicturePath) VALUES (?, ?, ?);""", (x,hashedPassword,"defaultProfile.jpg"))
            connection.commit()
            st.success("User successfully registered!")
            return True
        else:
            st.warning("Username already taken! Please try another one!")
        return False

def loginUser(x, y):
    if not usernameChecker(x):
        st.warning("Username was not found, please check again or sign up")
        return False
    else:
        if passwordChecker(y, x):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Incorrect password, please try again!")
            return False