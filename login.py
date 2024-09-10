import streamlit as st
import time
import pyautogui
# st.stop() 

def Login():
    with st.form("my_form"):
        st.write("BGV Admin Panel")    
        
        # Add input fields
        username = st.text_input("username",placeholder="Enter username")
        password = st.text_input("Password",type="password",placeholder="Enter Password")
        # Add a submit button
        submitted = st.form_submit_button("Submit")
        
        # Form submission handler
        if submitted:
            if(username == "admin" and password == "admin"):
                for x in range(0,2):
                    st.success("Login Success Please wait")
                    print(username);
                    st.session_state.page = "Dashboard";
                    time.sleep(2)
                    pyautogui.press('enter')
                
                
            else:
                st.error("invalid credentials")
