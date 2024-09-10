import streamlit as st
from pymongo import MongoClient



def AddCandidate():

    client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
    db = client["BGC"] 
    
    with st.form("add_candidate"):
        st.write("Add Candidate")    
        emp_code = st.text_input("EMP Code")
        entity_code = st.text_input("Entity Code")
        candidate_name = st.text_input("Candidate Name")
        candidate_email = st.text_input("Candidate Email")
        candidate_phone = st.text_input("Candidate Phone")
        father_name = st.text_input("Father Name")
        dob = st.date_input("DOB")
        
        bgv_pan_number = st.text_input("PAN Number")
        bgv_aadhaar_number = st.text_input("Aadhaar Number")
        bgv_address = st.text_area("Address")
        gender = st.selectbox("Select Gender",["Male","Female"])
        options = ["Address", "Aadhar", "PAN","Employment","Educational","Court","Reference","Global Database","CIBIL"]
        bgv = st.multiselect("Please Select the BGV AREA",options=options)
        
        submitted = st.form_submit_button("Add Candidate")

        if submitted:

            t1 = { 
                "emp_code":emp_code, 
                "entity_code":entity_code, 
                "candidate_name":candidate_name, 
                "candidate_email":candidate_email, 
                "candidate_phone":candidate_phone, 
                "father_name":father_name, 
                "dob":str(dob), 
                "bgv_pan_number":bgv_pan_number, 
                "bgv_aadhaar_number":bgv_aadhaar_number, 
                "bgv_address":bgv_address, 
                "gender":gender,
                "bgv":bgv, 
            }
            a = db["authentication"].insert_one(t1)
            if a :
                st.success("Candidate Entery Successfull")
            