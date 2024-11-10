import streamlit as st
from pymongo import MongoClient
import datetime as dt

client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
db = client["BGV"]["auth"]

def addressCheck():
    st.title("Address Verification Form")

    # Columns for the form
    col1, col2, col3 = st.columns(3)

    # First row
    with col1:
        address_type = st.selectbox("Address Type*", ["Residential", "Commercial", "Other"], key="address_type")
    with col2:
        residence_type = st.selectbox("Residence Type*", ["Owned", "Rented", "Other"], key="residence_type")
    with col3:
        best_day_to_visit = st.text_input("Best day to visit (Mon–Sat)", key="best_day_to_visit")

    # Second row
    with col1:
        best_time_to_visit = st.text_input("Best Time to visit", key="best_time_to_visit")
    with col2:
        house_number = st.text_input("House no./Bldg no./Flat No.*", key="house_number")
    with col3:
        street_name = st.text_input("Street/Lane/Road*", key="street_name")

    # Third row
    with col1:
        area_locality = st.text_input("Area/Locality/ Sector*", key="area_locality")
    with col2:
        village_town_city = st.text_input("Village/Town/City*", key="village_town_city")
    with col3:
        district = st.text_input("District*", key="district")

    # Fourth row
    with col1:
        state = st.text_input("State*", key="state")
    with col2:
        pincode = st.text_input("Pincode*", key="pincode")
    with col3:
        landmark = st.text_input("Landmark*", key="landmark")

    # Fifth row
    with col1:
        stay_from = st.date_input("Stay From*", key="stay_from")
    with col2:
        stay_to = st.date_input("Stay To*", key="stay_to")

    # Checkbox for permanent address
    same_as_residential_address = st.checkbox("Is your Permanent Address same as Residential Address?", key="same_as_residential_address")

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
    if st.button("Submit"):
        st.success("Hello world")
