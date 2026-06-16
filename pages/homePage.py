import streamlit as st
st.set_page_config(layout="wide")
def getUserProfilePicture():
    with open('pages/textFiles/userImages.txt', 'r') as f:
        for i in f:
            username, imagePath = i.strip().split(",")
            if username == st.session_state.get('username'):
                return imagePath
            return None

if not st.session_state.get("isUserLoggedIn"):
    st.error("Please log in first to access the page!")
    if st.button("Click here to login!"):
        st.switch_page("pages/loginPage.py")
else:
    st.text_input("", placeholder="Find user", key="userFinder")
    st.title(f"Hello {st.session_state.username.capitalize()}! This is the Home Page!")
    st.image(f"pages/images/{getUserProfilePicture()}")
    if st.button("My Profile", key="myProfileButton"):
        st.switch_page("pages/profilePage.py")
    st.html(body="""<style> .st-key-userFinder {
                                  position: fixed;
                                  top: 2.5vw;
                                  width: 66vw;
                                  right: 28vw;}
                            .st-emotion-cache-7czcpc.ehg91i91 img {
                                  width: 100px;
                                  height: 100px;
                                  aspect-ratio: 1 / 1;
                                  border-radius: 50%;
                                  object-fit: cover;
                                  position: relative;
                                  left: 75vw;
                                  bottom: 17vh;
                            }
                            .st-key-myProfileButton button {
                                  position: relative;
                                  bottom: 28vh;
                                  left: 83vw;
                                  border: 0;
                            
                            }
                            </style>""")