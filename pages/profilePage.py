import streamlit as st
from pathlib import Path
import os

fileList = []
if not st.session_state.get("isUserLoggedIn"):
    st.warning("Please login first")
else:
    uploadedFile = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploadedFile:
        counter = 0
        for i in Path('pages/images').iterdir():
            counter += 1
        fileType = uploadedFile.name.split('.')
        path = f"pages/images/{counter}.{fileType[1]}"
        with open(path, "wb") as f:
            f.write(uploadedFile.getvalue())
        with open('pages/textFiles/userImages.txt', 'r') as f:
            f.seek(0)
            for i in f:
                fileList.append(i.strip())
        for i in fileList:
            username, imagePath = i.strip().split(',')
            if imagePath != 'defaultProfile.jpg':
                os.remove(f"pages/images/{imagePath}")
            with open('pages/textFiles/userImages.txt', 'w') as f:
                f.write(f"{username},{counter}.{fileType[1]}")