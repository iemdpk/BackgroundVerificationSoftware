import streamlit as st
import login
from Check import dashboard;


if 'page' not in st.session_state:
    st.session_state.page = "Login"


if st.session_state.page == "Login":
    login.Login()
elif st.session_state.page == "Dashboard":
    dashboard.Dashboard()
