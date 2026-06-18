import streamlit as st
import sqlite3 as sql

st.set_page_config(layout="wide")
def getUserProfilePicture():
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT profilePicturePath FROM users WHERE username = ?", (st.session_state.username,))
        profilePicturePath = cursor.fetchone()[0]
        return profilePicturePath

if not st.session_state.get("isUserLoggedIn"):
    st.error("Please log in first to access the page!")
    if st.button("Click here to login!"):
        st.switch_page("pages/loginPage.py")
else:
    selectedUser = st.text_input("", placeholder="Find user", key="userFinder")
    if selectedUser:
        st.session_state.selectedUser = selectedUser
        st.switch_page("pages/profileOfUserChosen.py")

    st.title(f"Hello {st.session_state.username.capitalize()}! This is the Home Page!")
    st.image(f"pages/images/{getUserProfilePicture()}")
    if st.button("My Profile", key="myProfileButton"):
        st.switch_page("pages/profilePage.py")

    if st.button("Logout", key="logoutButton"):
        st.session_state.isUserLoggedIn = False
        st.session_state.username = ""
        st.switch_page("pages/homePage.py")
    st.html(body="""<style> .st-key-userFinder {
                                  position: fixed;
                                  top: 2.5vw;
                                  width: 66vw;
                                  right: 28vw;}
                            .st-emotion-cache-7czcpc.ehg91i91 img {
                                    position: fixed;
                                    top: 60px;
                                    right: 220px;
                                
                                    width: 100px !important;
                                    height: 100px;
                                    border-radius: 50%;
                                    object-fit: cover;
                            }
                            .st-key-myProfileButton button {
                                        position: fixed;
                                        top: 80px;
                                        width: 100px;
                                        right: 70px;
                                    }
                                    
                                    .st-key-logoutButton button {
                                        position: fixed;
                                        top: 130px;
                                        right: 83px;
                                        width: 70px;
                                    }
                            </style>""")