import streamlit as st
import sqlite3 as sql
import os
import functions
import bcrypt as b

if not st.session_state.get("isUserLoggedIn"):
    st.warning("Please login first")
else: # Everything below will only run if user is logged in
    uploadedFile = st.file_uploader("Change profile picture", type=["png", "jpg", "jpeg"], max_upload_size=10)
    if uploadedFile:
        with open(os.path.join("pages/images", uploadedFile.name), "wb") as f:
            f.write(uploadedFile.getvalue())
            os.rename(os.path.join("pages/images", uploadedFile.name),
                      os.path.join("pages/images", f"{st.session_state.get("username")}.png"))
        with sql.connect("project_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
            currentProfilePicture = cursor.fetchone()[0]
            cursor.execute(f"UPDATE users SET profilePicturePath = ? WHERE username = ?",
                               (f"{st.session_state.get("username")}.png", st.session_state.get("username"),))

    # Getting the user's current profile picture
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT profilePicturePath from users WHERE username = ?", (st.session_state.username,))
        col1, col2 = st.columns(2, width=600)
        profilePicture = cursor.fetchone()[0]
        st.image(f"pages/images/{profilePicture}")

        col1, col2 = st.columns(2, width=600)
        with col1:
            desiredUsername = st.text_input("Change username", placeholder="Enter username", width=300)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Confirm"):
               if desiredUsername == "":
                   st.warning("Please enter a username")
               else:
                   if functions.usernameChecker(desiredUsername):
                       st.warning("Username already taken")
                   else:

                       if desiredUsername.isalnum():
                           cursor.execute("UPDATE users set Username = ? WHERE username = ?", (desiredUsername, st.session_state.username))
                           if profilePicture != "defaultProfile.jpg":
                               os.rename(os.path.join("pages/images", f"{st.session_state.get("username")}.png"), os.path.join("pages/images", f"{desiredUsername}.png"))
                               cursor.execute("UPDATE users set profilePicturePath = ? WHERE username = ?", (f"{desiredUsername}.png", desiredUsername))
                           st.success("Username changed")
                           st.session_state.username = desiredUsername
                       else:
                           st.error("Username cannot contain symbols or space")

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
    def clickedButton():
        st.session_state.button_clicked = True
    st.button("Change password", on_click=clickedButton)
    if st.session_state.button_clicked:
            currentPasswordChecker = st.text_input("Current Password", placeholder="Enter your current password", width=300, type="password")
            col1, col2 = st.columns(2, width=600)
            with col1:
                changedPassword = st.text_input("Choose new password", placeholder="Enter a new password", width=300, type="password")
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                submitNewPassword = st.button("Change")

            if submitNewPassword:
                with sql.connect("project_data.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute("SELECT password from users WHERE username = ?", (st.session_state.username,))
                    hashedPassword = cursor.fetchone()[0]

                    if b.checkpw(currentPasswordChecker.encode('utf-8'), hashedPassword.encode('utf-8')):
                        st.success("Password changed")
                        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (b.hashpw(changedPassword.encode('utf-8'), b.gensalt()).decode('utf-8'), st.session_state.username))
                        connection.commit()
                        st.session_state.button_clicked = False
                    else:
                        st.warning("Current password is incorrect")
                        st.session_state.button_clicked = False


    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT aboutMe from users WHERE username = ?", (st.session_state.get("username"),))
        userAboutMe = cursor.fetchone()[0]
    desiredAboutMe = st.text_area(label="About me", max_chars=200, height=200, width=600, value=userAboutMe)
    if st.button("Submit"):
        st.success("Your About Me has been changed!")
        with sql.connect("project_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE users set aboutMe = ? WHERE username = ?", (desiredAboutMe, st.session_state.get("username")))


    st.html("""<style>
    .st-emotion-cache-h5555q {
        min-height: 0;
        height: 0;
        padding: 0;
        display: inline-block;
    }
    
    .st-emotion-cache-7czcpc {
        width: 100px;
        height: 100px;
        position: absolute
    }
    
    .st-emotion-cache-7czcpc > img {
                 width: 100px !important;
                 height: 100px;
                 position: absolute !important;
                 left: 150px;
                 bottom: 120px;
                 aspect-ratio: 1;
                 border-radius: 50%;
                 object-fit: cover;
    }
    
    .st-emotion-cache-jwhd0x {
        min-height: 0;
        height: 0;
        padding: 0;
        display: inline-block;
    }
    </style>""")