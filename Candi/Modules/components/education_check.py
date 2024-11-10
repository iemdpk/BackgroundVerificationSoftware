import streamlit as st
from pymongo import MongoClient
import datetime as dt


client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
db = client["BGV"]["Education"]

def education_Check():
    st.title("Education Verification Form")

    education_level = st.selectbox(
        "Course Name* (Please fill details relevant to the highest degree)",
        options=["10th", "12th", "Graduation", "Post Graduation", "Others (Specify)"],
        key="education_level"
    )

    col1, col2, col3 = st.columns(3)


    with col1:
        program = st.selectbox("Program*", ["Bachelors", "Masters", "Diploma", "Certificate", "Other"], key="program")
    with col2:
        completion_status = st.selectbox("Completed*", ["Yes", "No"], key="completion_status")


    with col1:
        student_id = st.text_input("Student ID / Enrollment No. / Roll No.", key="student_id")
    with col2:
        institute_name_address = st.text_input("Institute Name & Address", key="institute_name_address")


    with col1:
        institute_contact = st.text_input("Institute Email Id & Phone Number", key="institute_contact")
    with col2:
        university_name = st.text_input("University Name", key="university_name")


    with col1:
        degree_name = st.text_input("Degree Name", key="degree_name")
    with col2:
        specialization_subject = st.text_input("Subject (Specialization / Major)", key="specialization_subject")


    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("From (dd/mm/yy)", key="start_date")
    with col2:
        end_date = st.date_input("To (dd/mm/yy)", key="end_date")

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

    if st.button("Add Education"):
        asyncData = st.session_state.username;

        a = {"education_level":education_level,
        "program":program,
        "completion_status":completion_status,
        "student_id":student_id,
        "institute_name_address":institute_name_address,
        "institute_contact":institute_contact,
        "university_name":university_name,
        "degree_name":degree_name,
        "specialization_subject":specialization_subject,
        "start_date":str(start_date),
        "end_date":str(end_date),
        "email":asyncData["email"],
        "user_id":asyncData["_id"],
        "submbitted_at":dt.datetime.now()
        }
        if db.insert_one(a):
            st.success("Education is Inserted")
            st.rerun()
                

