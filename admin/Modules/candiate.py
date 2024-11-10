import streamlit as st
from pymongo import MongoClient
import pandas as pd
import datetime

st.set_page_config(layout="centered", page_title="Add Candidate")

def candidate():
    
    client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
    db = client["BGV"]["auth"]

    all_data = db.find();
    
    d1 = [];
    for document in all_data:
        d1.append(document)



    st.subheader("Assign Verification Type")
    st.text("")
    cols = st.columns(4)

    cheque = [];

    with cols[0]:
        education =  st.checkbox("Education Check")
        if education:
            cheque.append("Education Check")

        reference = st.checkbox("Reference Check")
        if reference:
            cheque.append("Reference Check")
        drug = st.checkbox("Drug Check")
        if drug :
            cheque.append("Drug Check")

    with cols[1]:
        address =  st.checkbox("Address Check")
        if address:
            cheque.append("Address Check")
        employment = st.checkbox("Employment Check")
        if employment:
            cheque.append("employment Check")
        credit =  st.checkbox("Credit Check")
        if credit:
            cheque.append("Credit Check")

    with cols[2]:
        criminal =  st.checkbox("Criminal Check(Ecourts)")
        if criminal:
            cheque.append("Criminal Check(Ecourts)")
        law_firm = st.checkbox("Criminal Check(Law Firm)")
        if law_firm:
            cheque.append("Criminal Check(Law Firm)")

    with cols[3]:
        identity =  st.checkbox("Identity Check")
        if identity:
            cheque.append("Identity Check")

        database = st.checkbox("Database Check(India / Global)")
        if database:
            cheque.append("database  Check(India / Global)")


    if 'textEmail' not in st.session_state:
        st.session_state.textEmail = ""
    
    textEmail = st.text_area(placeholder="Enter all emain",label="Enter Email",value=st.session_state.textEmail)


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
    if st.button("Add Candidate"):
        inserted = { "email":textEmail,"bgv_checks" : cheque,"Status":"Draft","created_at":datetime.datetime.now()}
        db.insert_one(inserted);
        st.toast("candidate send email")
        st.session_state.textEmail = ""
        st.rerun()
    st.divider()
    
    # Sample DataFrame
    df = pd.DataFrame(d1)

    # Display the DataFrame with buttons for each row
    st.write("Candidates:")

    event = st.dataframe(df,on_select="rerun",selection_mode="single-row")


    try:
        if event.selection.rows[0] == 0:
            st.toast("You Selected Me")
    except:
        print("none")    
    
