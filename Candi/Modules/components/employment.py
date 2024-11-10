import streamlit as st
from datetime import date
import random

def employment_check():
    st.header("Employment Check")

    # Self Employed and Nature of Employment selection
    self_employed = st.selectbox("Self Employed *", ["Select", "Yes", "No"])
    nature_of_employment = st.selectbox("Nature of Employment *", ["Select", "Permanent", "Contractual", "Internship", "Other"])

    # Text inputs for designations and department
    current_designation_official = st.text_input("Current Designation (Official Title)")
    current_designation_functional = st.text_input("Current Designation (Functional Title)")
    dept_project = st.text_input("Dept. / Project")

    # Company details
    company_name = st.text_input("Company (as stated on salary slip)")
    head_office_address = st.text_input("Address & Phone Number (Head Office)")
    address_phone = st.text_input("Address & Phone Number")

    # Employment tenure and employee code
    tenure_from_date = st.date_input("Employment Tenure (From Date)", min_value=date(1900, 1, 1))
    tenure_to_date = st.date_input("Employment Tenure (To Date)", min_value=date(1900, 1, 1))
    employee_code = st.text_input("Employee Code")

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
    if st.button("Submit",key=random.randint(11111111111,99999999999)):
        st.success("Employment details submitted successfully.")

# Run the employment_check function
if __name__ == "__main__":
    employment_check()
