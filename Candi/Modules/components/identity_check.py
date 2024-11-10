import streamlit as st
from pymongo import MongoClient
import datetime as dt


client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
db = client["BGV"]["auth"]



st.set_page_config(layout="wide", page_title="Add Candidate")
def identity_check():
    st.subheader("Candidate Declaration From")
    st.divider()
    profilePicture = st.file_uploader("Upload Profile Picture")
    colum = st.columns([3, 3, 3], gap="medium")
    
    with colum[0]:
        fullName = st.text_input("Enter Full Name")
        placeOfBirth = st.text_input("Enter Place of Birth")
        nationatility = st.text_input("Enter Nationality")
        number = st.number_input("Enter Mobile")
        

    with colum[1]:
        FatherName = st.text_input("Enter Father Name")
        gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
        aadhar = st.number_input("Enter AAdhar Number",placeholder="")
       

    with colum[2]:
        dob = st.date_input("Enter Date of Birth")
        maritial_status = st.selectbox("Maritial Status", ["Married", "UnMarried"])
        passport = st.number_input("Enter Passport Number",placeholder="")
        

    criminal_offence = st.selectbox("Have you ever been convicted of any criminal offence in India or outside India?", ["No", "Yes"])
    if criminal_offence == "Yes":
        details_of_conviction = st.text_area("Please provide details of conviction")
    st.markdown(
    """
    <style>
    .element-container:has(#button-after) + div button {
        background-color: red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

    if st.button("Submit the Details"):
        asyncData = st.session_state.username;
        print(asyncData)
        a = {
        "fullName": fullName,
        "placeOfBirth": placeOfBirth,
        "nationality": nationatility,
        "mobileNumber": number,
        "fatherName": FatherName,
        "gender": gender,
        "aadharNumber": aadhar,
        "dateOfBirth": str(dob),
        "maritalStatus": maritial_status,
        "passportNumber": passport,
        "criminalOffence": criminal_offence,
        "convictionDetails": details_of_conviction if criminal_offence == "Yes" else "",
        "profilePicture": profilePicture,
        "declarationDate": dt.datetime.now(),
        "user_id":asyncData["_id"],
      }
        print("This is All Value ")
        print(a);
        if db.update_one({"email":asyncData["email"]},{"$set":a}):
            st.success("This is Saved")

    