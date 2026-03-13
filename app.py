import streamlit as st

st.set_page_config(page_title="Simple Browser", layout="wide")

if "url" not in st.session_state:
    st.session_state.url = "https://www.google.com"

st.title("Python Streamlit Browser")

col1, col2, col3 = st.columns([6,1,1])

with col1:
    url = st.text_input("Enter URL", st.session_state.url)

with col2:
    if st.button("Go"):
        st.session_state.url = url

with col3:
    if st.button("Refresh"):
        st.session_state.url = url

st.components.v1.iframe(st.session_state.url, height=800, scrolling=True)
