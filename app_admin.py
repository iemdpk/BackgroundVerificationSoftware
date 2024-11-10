import streamlit as st
from admin.mode import login  
from admin.mode import sidebar

if 'route' not in st.session_state:
    st.session_state.route = "/"

if st.session_state.route == "/":
    login.Login() 
elif st.session_state.route == "dashboard":
    sidebar.Sidebar()

