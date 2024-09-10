import streamlit as st


def AddCandidate():
    
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
        st.multiselect("Please Select the BGV AREA",options=options)
        
        submitted = st.form_submit_button("Add Candidate")

        if submitted:

            st.write("Candidate added successfully!")
            st.write(f"Candidate Name: {candidate_name}")
            st.write(f"Candidate Email: {candidate_email}")
            st.write(f"Candidate Phone: {candidate_phone}")
            st.write(f"BGV PAN Number: {bgv_pan_number}")
            st.write(f"BGV Aadhaar Number: {bgv_aadhaar_number}")
            st.write(f"BGV Address: {bgv_address}")