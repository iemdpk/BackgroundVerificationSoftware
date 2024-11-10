import streamlit as st
import time
# import pyautogui
# st.stop() 

def Login():
    
    with st.form("my_form"):
        st.write("BGV Admin Panel")    
        username = st.text_input("username",placeholder="Enter username")
        password = st.text_input("Password",type="password",placeholder="Enter Password")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if(username == "admin" and password == "admin"):
                for x in range(0,1):
                    st.success("Login Success Please wait")
                    st.session_state.route = "dashboard"
                    print("This is Route page "+st.session_state.route);
                    st.rerun()
                    print(username);
                    print("This is Login Guys");
                    time.sleep(2)
            else:
                st.error("invalid credentials")


Login()