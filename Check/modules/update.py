import streamlit as st
from pymongo import MongoClient

def update():
    
    client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
    db = client["BGC"] 
    a = db["authentication"].find_one({"emp_code":"02"})
    # a = db.find_one({emp_code:"EMP-01"})
    st.title( "upload your Documents here "+a["candidate_name"]);
    
    

     
    
    