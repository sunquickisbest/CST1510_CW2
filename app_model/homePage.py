import streamlit as st
import sqlite3 as sql
from groq import Groq
from dotenv import load_dotenv
import os

from streamlit import container

### Load AI
load_dotenv("api.env")
apiKey = os.environ.get("GROQ_API_KEY")
Client = Groq(api_key=apiKey)
###

st.set_page_config(layout="wide")
def getUserProfilePicture():
    with sql.connect("DATA/project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT profilePicturePath FROM users WHERE username = ?", (st.session_state.username,))
        profilePicturePath = cursor.fetchone()[0]
        return profilePicturePath

#### Prevent the user from accessing the Home Page if they're not logged in
if not st.session_state.get("isUserLoggedIn"):
    st.error("Please log in first to access the page!")
    if st.button("Click here to login!"):
        st.switch_page("app_model/loginPage.py")
###
else:
    ### Bar to find user
    with container(key="FindUserInput"):
        selectedUser = st.text_input("", placeholder="Find user", key="userFinder")
    ###

    ### User's profile picture
    with st.container(key="ProfilePicture"):
        st.image(f"DATA/images/{getUserProfilePicture()}")
    ###

    ### If user is searching for user, set session state of selected user and change the page
    if selectedUser:
        st.session_state.selectedUser = selectedUser
        st.switch_page("app_model/profileOfUserChosen.py")
    ###


    st.title(f"Hello {st.session_state.username.capitalize()}! This is the Home Page!")

    ### The buttons next to the user's profile picture
    with st.container(key="UserInfoButtons"):
        if st.button("My Profile", key="myProfileButton"):
            st.switch_page("app_model/profilePage.py")
        if st.button("Logout", key="logoutButton"):
            st.session_state.isUserLoggedIn = False
            st.session_state.username = ""
            st.switch_page("app_model/homePage.py")
    ###

    ### Tabs for datasets
    tab1, tab2, tab3 = st.tabs(["Cyber Incidents", "IT Tickets", "Metadata Page"])
    with tab1:
        st.header("Cyber Incidents")
        with open("app_model/logic/Cyber_Incidents.py", "r") as file:
            exec(file.read())
    with tab2:
        st.header("IT Tickets")
        with open("app_model/logic/IT_Tickets.py", "r") as file:
            exec(file.read())
    with tab3:
        st.header("Metadata Page")
        with open("app_model/logic/Metadata.py", "r") as file:
                exec(file.read())
    ###

    ### The AI chat
    with st.container(key="AIContainer"):
        if 'messages' not in st.session_state:
            st.session_state.messages = [{"role" : "system", "content" : """You are to act exclusively as a Senior Cybersecurity Consultant, providing expert-level advice on information security, threat intelligence, vulnerability management, and defensive architecture. You must maintain a professional and objective tone at all times, focusing solely on providing precise, actionable technical guidance related to these fields. If a user asks a question, requests information, or attempts to engage in conversation that falls outside the scope of cybersecurity, you must respond with exactly: "Not in my domain." Furthermore, if any inquiry involves unethical or illegal activities, you are to strictly refuse to provide harmful information and instead explain the security controls and defensive principles that mitigate such risks."""}]

        prompt = st.chat_input("Say something to the AI")

        with st.chat_message("assistant"):
            st.write("Hello! I'm a Cybersecurity assistant. How can I help you?")
        if prompt: # If message entered, run code below
            st.session_state.messages.append({"role" : "user", "content" : prompt})
            Chat = Client.chat.completions.create(messages=st.session_state.messages, model="llama-3.3-70b-versatile")
            st.session_state.messages.append({"role":"assistant", "content":Chat.choices[0].message.content})
        for i in st.session_state.messages:
            if i["role"] == "system":
                continue
            st.chat_message(i["role"]).write(i["content"])



    st.html(body="""<style> 
                            .st-key-CloseButton div {
                                position: relative;
                                left: 0;
                            }
                            
                            .st-key-userFinder {
                                  position: relative;
                                  bottom: 20px;
                            }
                            
                            .st-key-FindUserInput div {
                                 width: 66vw !important;
                            }
                            .st-emotion-cache-4rsbii {
                                overflow-x: hidden;
                            }
                                  
                            .st-key-ProfilePicture {
                                display: flex;
                                align-items: end;
                                min-height: 20px;
                                height: 20px !important;
                            }
                            
                            .st-emotion-cache-1n6tfoc {
                                flex:none;
                            }
      
                            .st-key-ProfilePicture img {
                                position: relative;
                                right: 170px;
                                bottom: 90px;
                                width: 100px !important;
                                height: 100px;
                                border-radius: 50%;
                                object-fit: cover;
                            }
                            .st-key-UserInfoButtons {
                                width: 100%;
                                position: relative;
                                left: 100vw;
                            }

                            .st-key-myProfileButton button {
                                position: absolute;
                                bottom: 160px;
                                width: 100px;
                                right: 210px;
                            }
                                    
                            .st-key-logoutButton button {
                                position: absolute;
                                right: 220px;
                                bottom: 130px;
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
                            
                            .st-key-AIContainer p{
                                text-align: left;
                                position: static;
                            }
                            
                            .st-key-AIContainer button{
                                position: relative;
                            }
                            
                            .st-key-AIContainer {
                                background-color: #44444E;
                                padding: 18px;
                                border-radius: 20px;
                                position: absolute;
                                bottom: 0px;
                                right: 30px;
                                width: 340px;
                                height: 350px;
                                overflow-y: scroll;
                            }
                            
                            </style>""")