import streamlit as st
import requests

# API endpoint from backend
API_ENDPOINT = "http://localhost:5000/upload"

st.title("📥 Telugu LLM Data Uploader")
st.markdown("Upload audio, video, image, or text files to contribute to Telugu datasets.")

# Input fields
title = st.text_input("Enter title")
description = st.text_area("Description (optional)")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a file to upload", 
    type=["mp3", "wav", "mp4", "jpg", "png", "txt", "pdf"]
)

# Submit button
if st.button("Upload"):
    if uploaded_file is None or not title:
        st.warning("Please upload a file and enter the title.")
    else:
        files = {"file": (uploaded_file.name, uploaded_file)}
        data = {"title": title, "description": description}
        try:
            response = requests.post(API_ENDPOINT, data=data, files=files)
            if response.status_code == 200:
                st.success("✅ File uploaded successfully!")
            else:
                st.error(f"❌ Upload failed: {response.status_code}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")
