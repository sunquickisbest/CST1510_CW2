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
    st.image(f"pages/images/{getUserProfilePicture()}")
    if selectedUser:
        st.session_state.selectedUser = selectedUser
        st.switch_page("pages/profileOfUserChosen.py")

    st.title(f"Hello {st.session_state.username.capitalize()}! This is the Home Page!")
    if st.button("My Profile", key="myProfileButton"):
        st.switch_page("pages/profilePage.py")

    if st.button("Logout", key="logoutButton"):
        st.session_state.isUserLoggedIn = False
        st.session_state.username = ""
        st.switch_page("pages/homePage.py")


    tab1, tab2, tab3 = st.tabs(["Cyber Incidents", "IT Tickets", "Metadata Page"])
    with tab1:
        st.header("Cyber Incidents")
        with open("pages/Cyber_Incidents.py", "r") as file:
            exec(file.read())
    with tab2:
        st.header("IT Tickets")
        with open("pages/IT_Tickets.py", "r") as file:
            exec(file.read())
    with tab3:
        st.header("Metadata Page")
        with open("pages/Metadata.py", "r") as file:
                exec(file.read())
    st.html(body="""<style> 
                            .st-key-userFinder {
                                  position: relative;
                                  bottom: 20px;
                            }
                            
                            .eiqkja70 {
                             width: 66vw !important;
                            }
                                  
                            .st-emotion-cache-7czcpc.ehg91i91 {
                                position: absolute;
                                left: 100vw !important;
                                width: 100px !important;
                                height: 100px !important;
                            }
      
                            .st-emotion-cache-7czcpc.ehg91i91 img {
                                position: absolute;
                                right: 400px;
                                bottom: 100px;
                                
                                width: 100px !important;
                                height: 100px;
                                border-radius: 50%;
                                object-fit: cover;
                            }
                            .e150o2y10 {
                                width: 100%;
                                position: absolute;
                                left: 100vw;
                            }

                            .st-key-myProfileButton button {
                                        position: absolute;
                                        bottom: 150px;
                                        width: 100px;
                                        right: 170px;
                                    }
                                    
                            .st-key-logoutButton button {
                                        position: absolute;
                                        right: 180px;
                                        bottom: 120px;
                                        width: 70px;
                                    }
                            
                            .stFormSubmitButton{
                                position: relative;
                                left: 0px;
                                bottom: 25px;
                            
                            }
                                    
                            .st-key-addIncidentButton button {
                                position: relative;
                                        top: 30px;
                                        width: 130px;
                            }
                            </style>""")