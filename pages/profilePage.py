import streamlit as st
import sqlite3 as sql
import os

if not st.session_state.get("isUserLoggedIn"):
    st.warning("Please login first")
else: # This part below will only run if user is logged in
    uploadedFile = st.file_uploader("Change profile picture", type=["png", "jpg", "jpeg"], max_upload_size=10)
    if uploadedFile:
        with open(os.path.join("pages/images", uploadedFile.name), "wb") as f:
            f.write(uploadedFile.getvalue())
            os.rename(os.path.join("pages/images", uploadedFile.name), os.path.join("pages/images",f"{st.session_state.get("username")}.png"))
        with sql.connect("project_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
            currentProfilePicture = cursor.fetchone()[0]
            cursor.execute(f"UPDATE users SET profilePicturePath = ? WHERE username = ?", (f"{st.session_state.get("username")}.png",st.session_state.get("username"),))


    # Getting the user's current profile picture
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
        profilePicture = cursor.fetchone()[0]
    st.image(f"pages/images/{profilePicture}")
    st.html("""<style>
    .st-emotion-cache-h5555q {
        min-height: 0;
        height: 0;
        padding: 0;
        display: inline-block;
    }
    
    .st-emotion-cache-7czcpc > img {
                 width: 100px !important;
                 height: 100px;
                 position: fixed;
                 left: 18vw;
                 bottom: 75vh;
                 aspect-ratio: 1;
                 border-radius: 50%;
                 object-fit: cover;
    }
    </style>""")