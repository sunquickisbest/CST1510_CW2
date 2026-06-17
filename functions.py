import streamlit as st
import bcrypt as b
import sqlite3 as sql

def passwordChecker(x):
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT password FROM users WHERE username = ?""", (x,))
        passwordCheck = cursor.fetchone()
        if passwordCheck is not None and b.checkpw(x.encode('utf-8'), passwordCheck[0].encode('utf-8')):
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
        if passwordChecker(y):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Incorrect password, please try again!")
            return False