import streamlit as st
import sqlite3 as sql
import os

if not st.session_state.get("isUserLoggedIn"):
    st.warning("Please login first")
else: # This part below will only run if user is logged in
    uploadedFile = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploadedFile:
        with open(os.path.join("pages/images", uploadedFile.name), "wb") as f:
            f.write(uploadedFile.getvalue())
            os.rename(os.path.join("pages/images", uploadedFile.name), os.path.join("pages/images",f"{st.session_state.get("username")}.png"))
        with sql.connect("project_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
            currentProfilePicture = cursor.fetchone()[0]
            cursor.execute(f"UPDATE users SET profilePicturePath = ? WHERE username = ?", (f"{st.session_state.get("username")}.png",st.session_state.get("username"),))