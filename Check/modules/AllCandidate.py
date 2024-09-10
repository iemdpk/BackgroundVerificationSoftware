import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import numpy as np
from faker import Faker
import random
# Initialize Faker
fake = Faker()
Faker.seed(0)
from pymongo import MongoClient

def allCandidate():
        
        client = MongoClient("mongodb+srv://iemdpk:Imback2play@localserver.cwqbg.mongodb.net",tls=True,tlsAllowInvalidCertificates=True)
        db = client["BGC"]["authentication"]

        all_data = db.find();
        print("This is Deepak")
        d1 = [];
        for document in all_data:
            d1.append(document)
    
        df = pd.DataFrame(d1)
       
        st.title("Candidate DataTable")
        st.divider()
        st.write(df)

        st.title("Search Candidate")
        st.divider()
        search_query = st.text_input("Search by Name or EMP Code", "")
        st.divider()
       
       
        page_size = 5  # Number of rows per page
        # total_pages = (len(filtered_df) - 1) // page_size + 1
       
        def display_buttons(df):
            for index, row in df.iterrows():
                col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
                
                with col1:
                    st.write(f"{row["entity_code"]}-{row["emp_code"]} ({row["candidate_name"]})")  # Display row data or customize how to display it

                with col2:
                    if st.button(f"Status",key=index):
                        st.write(f"Button clicked for row {index}!")
                        # Here you can handle what happens when the button is clicked

        # Display buttons next to each row
        display_buttons(df)