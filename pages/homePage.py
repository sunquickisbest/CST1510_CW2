import streamlit as st
import sqlite3 as sql
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv("api.env")
apiKey = os.environ.get("GROQ_API_KEY")
Client = Groq(api_key=apiKey)

st.set_page_config(layout="wide")
def getUserProfilePicture():
    with sql.connect("project_data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT profilePicturePath FROM users WHERE username = ?", (st.session_state.username,))
        profilePicturePath = cursor.fetchone()[0]
        return profilePicturePath

##### Prevent the user from accessing the Home Page if they're not logged in #####
if not st.session_state.get("isUserLoggedIn"):
    st.error("Please log in first to access the page!")
    if st.button("Click here to login!"):
        st.switch_page("pages/loginPage.py")
##########
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

    ###### Tabs for different pages #####
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
    with st.container(key="AIContainer"):
        if 'messages' not in st.session_state:
            st.session_state.messages = [{"role" : "system", "content" : "As a dedicated cybersecurity expert, my sole professional focus is the identification, analysis, and mitigation of digital threats to ensure the integrity, confidentiality, and availability of information systems. I provide rigorous, technically precise guidance rooted in established security frameworks such as NIST, CIS Controls, and ISO/IEC 27001 to assist in hardening infrastructure against sophisticated attack vectors. My methodology prioritizes proactive risk assessment, the implementation of defense-in-depth strategies, and the continuous monitoring of network environments to detect anomalous behavior and potential breaches before they escalate. Whether addressing the complexities of identity and access management, the intricacies of cryptographic implementations, or the nuances of vulnerability management, I operate strictly within the domain of cybersecurity to maintain the highest standards of technical accuracy and defensive posture. Consequently, I am unable to deviate from this expertise or address inquiries outside the scope of cybersecurity, as my purpose is to provide specialized, domain-specific intelligence aimed at protecting digital assets against an evolving landscape of adversaries and systemic weaknesses. IF user goes out of topic just say Not in my Domain. and nothing else"}]

        prompt = st.chat_input("Say something...")

        with st.chat_message("assistant"):
            st.write("Hello! How can I help you today?")
        if prompt:
            st.session_state.messages.append({"role" : "user", "content" : prompt})
            Chat = Client.chat.completions.create(
                messages=st.session_state.messages, model="llama-3.3-70b-versatile"
            )
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
                                        right: 183px;
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
                            
                            .st-key-AIContainer p{
                                text-align: left;
                                position: static;
                            }
                            
                            .st-key-AIContainer button{
                                position: relative;
                            }
                            
                            .st-emotion-cache-1n6tfoc {
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