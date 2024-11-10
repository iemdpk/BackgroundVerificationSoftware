import streamlit as st
import time
import random
from pymongo import MongoClient
import asyncio


client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net", tls=True, tlsAllowInvalidCertificates=True)
db = client["BGV"]["auth"]


st.session_state.otp = None
if "otp" not in st.session_state:
    st.session_state.otp = None

def Login():
    
    with st.form("login_form"):
        st.write("BGV Candidate(Section)")    
        username = st.text_input("Email", placeholder="Enter Email")
        submitted = st.form_submit_button("Login")
        
    
        if submitted:
            st.session_state.otp = random.randint(1111, 9999)
            st.session_state.username = username
            st.success(f"OTP has been sent to {username}. (For testing: OTP is {st.session_state.otp})")

    
    if "otp" in st.session_state :
        otp_enter = st.text_input("OTP", placeholder="Enter OTP")
        verify_button = st.button("Verify")
        
        if verify_button:
            if otp_enter == str(st.session_state.otp):
                st.toast("Please wait we are fetching details!")
                time.sleep(2)
                emailFind = db.find_one({"email":st.session_state.username})
                if emailFind != None:
                    st.session_state.userDetails  = emailFind
                   
                    st.success("Email FInd")
                    st.session_state.route = "Dashboard"
                    st.rerun()
                else:
                    st.error("Email not found")       
            else:
                st.error("Incorrect OTP. Please try again.")

Login()
