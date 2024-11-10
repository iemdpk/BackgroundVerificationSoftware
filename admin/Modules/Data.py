import streamlit as st
from pymongo import MongoClient
import pandas as pd


def Dataframe():
    client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
    db = client["BGV"]["auth"]
    st.subheader("All Candidate")
    all_data = db.find();
    
    d1 = [];
    for document in all_data:
        d1.append(document)

    df = pd.DataFrame(d1)

    # Display the DataFrame with buttons for each row
    st.write("Candidates:")

    event = st.dataframe(df,on_select="rerun",selection_mode="single-row")

    
