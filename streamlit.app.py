import streamlit as st

if "auth" not in st.session_state:
        st.session_state["auth"] = False