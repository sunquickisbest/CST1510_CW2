import streamlit as st
import sqlite3 as sql
import os

if not st.session_state.get("isUserLoggedIn"):
    st.warning("Please login first")
else:
    uploadedFile = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploadedFile:
        counter = 0
        for i in os.listdir("pages/images"):
            counter += 1
        with open(os.path.join("pages/images", uploadedFile.name), "wb") as f:
            f.write(uploadedFile.getvalue())
            os.rename(os.path.join("pages/images", uploadedFile.name), os.path.join("pages/images",f"{counter}.png"))
        with sql.connect("project_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
            currentProfilePicture = cursor.fetchone()[0]
            if currentProfilePicture != "defaultProfile.jpg":
                os.remove(os.path.join("pages/images", currentProfilePicture))
            cursor.execute(f"UPDATE users SET profilePicturePath = ? WHERE username = ?", (f"{counter}.png",st.session_state.get("username"),))