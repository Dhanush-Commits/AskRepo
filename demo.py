import streamlit as st

# Access the API key
if "GOOGLE_API_KEY_1" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY_1"]
    st.write(f"API Key Loaded: {api_key}")  # Just for debugging
else:
    st.error("API Key not found!")
