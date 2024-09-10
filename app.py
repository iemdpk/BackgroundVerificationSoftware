import streamlit as st
import login
from Check import dashboard;
from Check.modules import update
from Check.modules import status


if 'page' not in st.session_state:
    st.session_state.page = "Login"

try:
    st.query_params["update_id"]
    update.update()
except:
    try:
        st.query_params["user_id"]
        status.status()
    except:
        
        if st.session_state.page == "Login":
            login.Login()
        elif st.session_state.page == "Dashboard":
            dashboard.Dashboard()
