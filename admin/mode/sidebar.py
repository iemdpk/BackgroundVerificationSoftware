import streamlit as st
from admin.Modules.Data import Dataframe
from admin.Modules.candiate import candidate
from pymongo import MongoClient
import pandas as pd


css = """
.ef3psqc13 {
    border: none !important;
}
"""

st.session_state.sidebar = "sidebar"

if "sidebar" not in st.session_state:
    st.session_state.sidebar = "sidebar"

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def Sidebar():
      
    def Candidate():
        st.session_state.sidebar = "Candidate"; 
        Dataframe()

    def Add():
        st.session_state.sidebar = "AddCandidate"; 
        candidate()

    def Dashboard():
        st.session_state.sidebar = "sidebar"; 
        
    st.sidebar.text("Routes")
    
    st.sidebar.button("Dashboard",use_container_width=True,on_click=Dashboard)
    st.sidebar.button("Candidate",use_container_width=True,on_click=Candidate)
    st.sidebar.button("Add Candidate / BGV",use_container_width=True,on_click=Add)
    

    if("sidebar" not in st.session_state or st.session_state.sidebar  == "sidebar"):
        st.subheader("Dashboard")
        
        cols = st.columns(2,gap="medium",vertical_alignment="center")  # Create 3 columns

        with cols[0]:
           
           
            total_selling = 1000.00
            delta_value = 500.00  # Example delta value

            # Create a styled div for the metric display
            st.markdown(
                f"""
                <div style="background-color: red;border-radius: 5px; text-align: center;">
                    <h2 style="color: white;">ALL CANDIDATE</h2>
                    <h3 style="color: white;">${total_selling:,.2f}</h3>
                    
                </div>
                """, 
                unsafe_allow_html=True
            )

        with cols[1]:
            st.markdown(
                f"""
                <div style="background-color: #34495e;border-radius: 5px; text-align: center;">
                    <h2 style="color: white;">REJECT CANDIDATE</h2>
                    <h3 style="color: white;">${total_selling:,.2f}</h3>
                    
                </div>
                """, 
                unsafe_allow_html=True
            )

        st.divider()
        client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
        db = client["BGV"]["auth"]
        st.subheader("All Candidate")
        all_data = db.find();
        
        d1 = [];
        for document in all_data:
            d1.append(document)

        df = pd.DataFrame(d1)
        event = st.dataframe(df,on_select="rerun",selection_mode="single-row")