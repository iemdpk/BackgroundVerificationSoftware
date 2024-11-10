import streamlit as st
from Candi.mode import login  
from Candi.mode import sidebar


if not hasattr(st.session_state, "sidebar"):
    st.session_state.sidebar = "sidebar"

    
if 'route' not in st.session_state:
    st.session_state.route = "dashboard"
    
    
if st.session_state.route == "/":
    login.Login() 
elif st.session_state.route == "dashboard":
    sidebar.Sidebar()

