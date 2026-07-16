import streamlit as st
import sqlite3 as sql

with sql.connect("DATA/project_data.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (st.session_state.selectedUser,))
    userInfo = cursor.fetchone()
if userInfo is None:
    st.error("User not found")
else:
    st.title("User Info:")
    st.write(userInfo[1])
    st.image(f"pages/images/{userInfo[3]}", width=200)
    st.text_area(label="About Me",value=userInfo[4], height=150, disabled=True, width=400, key="userInfo")


    st.html("""<style>.st-emotion-cache-4cktc5 p {
                            position:fixed;
                            top:300px;
                            left: 50%;
                            transform: translateX(-50%);
                    }
                      .st-emotion-cache-7czcpc > img {
                            width: 200px !important;
                            height: 200px;
                            position: fixed;
                            left: 50%;
                            transform: translateX(-50%);
                            top: 100px;
                            aspect-ratio: 1;
                            border-radius: 50%;
                            object-fit: cover;
                      }
                    .st-key-userInfo {
                        position: fixed;
                            left: 50%;
                            transform: translateX(-50%);
                            top: 330px;      
                    }         
    </style>""")