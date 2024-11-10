import streamlit as st
from Candi.Modules.candiate import candidate
from pymongo import MongoClient
import pandas as pd
from Candi.Modules.components import education_check,identity_check,address,refrence,employment,attachment
import random
client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net", tls=True, tlsAllowInvalidCertificates=True)
db = client["BGV"]["auth"]
username = db.find_one({"email":"m.deepak1825@gmail.com"})
if "username" not in st.session_state:
    st.session_state.username = username

css = """
.ef3psqc13 {
    border: none !important;
}
"""
def Sidebar():
    st.subheader("Please Fill All The  Details")
    for x in username["bgv_checks"]:
        with st.expander(x):
            if x == "Education Check":
                education_check.education_Check()
            elif x == "Identity Check":
                identity_check.identity_check()
            elif x == "Address Check":
                address.addressCheck()
            elif x == "Reference Check":
                refrence.refrence()
            elif x == "Drug Check":
                st.subheader("Drug Check Page Preparing")
            elif x == "Employment Check":
                employment.employment_check()
            elif x == "Attachments":
                attachment.document_upload()
            elif x == "Consent Form":
                st.text_input("Enter FIrst Name")
                st.text_input("Enter FIrst Last")

# with st.expander("Verification Status"):
#     st.write(username["Status"])
# with st.expander("BGV Checks"):
#     for x in username["bgv_checks"]:
#         st.write(x)

    

        
# st.session_state.sidebar = "sidebar"
# if "sidebar" not in st.session_state:
#     st.session_state.sidebar = "Education Check"

# st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# st.session_state.

# for x in username["bgv_checks"]:
#     st.sidebar.button(x,use_container_width=True,on_click=lambda check=x: candidate(check))

    
    # if st.sidebar.button("Submit for Review",use_container_width=True):
    #       st.success("It is Submitted")

    # if "sidebar" not in st.session_state or st.session_state.sidebar == "sidebar":
    #     st.subheader("Please fill all the routes")
        
    #     cols = st.columns(1,gap="medium",vertical_alignment="center")  # Create 3 columns

    #     with cols[0]:
           
           
    #         total_selling = 1000.00
    #         delta_value = 500.00  # Example delta value

    #         # Create a styled div for the metric display
    #         st.markdown(
    #             f"""
    #             <div style="background-color: red;border-radius: 5px; text-align: center;">
    #                 <h2 style="color: white;">Verification Status:</h2>
    #                 <h3 style="color: white;">{username["Status"]}</h3>
                    
    #             </div>
    #             """, 
    #             unsafe_allow_html=True
    #         )
    #         st.text_input("Enter FIrst asdName")
    #         st.text_input("Enter FIrst Last name")




       