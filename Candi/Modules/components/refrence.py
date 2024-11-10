import streamlit as st
from pymongo import MongoClient
import datetime as dt

client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
db = client["BGV"]["auth"]




def refrence():
    st.title("Background Verification - Reference Check")

    # Reference 1, 2, and 3 columns
    col_ref1, col_ref2, col_ref3 = st.columns(3)

    # Section Title for each column
    with col_ref1:
        st.subheader("Reference 1")
    with col_ref2:
        st.subheader("Reference 2")
    with col_ref3:
        st.subheader("Reference 3")

    # Fields for each reference
    fields = [
        "Name", 
        "Current Designation", 
        "Current Employer", 
        "Company name in which worked with the Reference", 
        "Personal Mobile No.", 
        "Email ID", 
        "Best time to reach"
    ]

    # Dictionary to hold the input variables for each reference
    reference_data = {f"{field}_ref{i}": None for i in range(1, 4) for field in fields}

    # Generate inputs for each reference in respective columns
    for i, col in enumerate([col_ref1, col_ref2, col_ref3], start=1):
        with col:
            for field in fields:
                key = f"{field.replace(' ', '_').lower()}_ref{i}"
                reference_data[key] = st.text_input(field, key=key)

    # Display submit button
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
    submit_button = st.button("Save Refrence")

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
    if submit_button:
        asyncData = st.session_state.username;
        a =  { "refrences" : reference_data,"crearted_date":dt.datetime.now()}
        if db.update_one({"email":asyncData["email"]},{"$set":a}):
            st.success("refrence is added")



