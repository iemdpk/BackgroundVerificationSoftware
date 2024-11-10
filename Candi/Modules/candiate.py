import streamlit as st
from pymongo import MongoClient
import pandas as pd
import datetime
from Candi.Modules.components import education_check,identity_check,address,refrence,employment,attachment

print("This is Running ");

def candidate(x):
    
    
    if "sidebar" not in st.session_state:
        st.session_state.sidebar = "sidebar"
        print("It is Declare")
    else:
        check_type =  st.session_state.sidebar
        if check_type == "Education Check":
            education_check.education_Check()
        elif check_type == "Identity Check":
            identity_check.identity_check()
        elif check_type == "Address Check":
             address.addressCheck()
        elif check_type == "Reference Check":
            refrence.refrence()
        elif check_type == "Drug Check":
            st.subheader("Drug Check Page Preparing")
        elif check_type == "Employment Check":
            employment.employment_check()
        elif check_type == "Attachments":
            attachment.document_upload()
        elif check_type == "Consent Form":
            st.text_input("Enter FIrst Name")
            st.text_input("Enter FIrst Last")
        else:
            print("erro")
        