import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import numpy as np
from faker import Faker
import random
# Initialize Faker
fake = Faker()
Faker.seed(0)

def allCandidate():
       
        num_records = 5
        data = {
            "EMP Code": [f"EMP{str(i).zfill(4)}" for i in range(1, num_records + 1)],
            "Entity Code": [f"ENT{random.randint(1, 10)}" for _ in range(num_records)],
            "Candidate Name": [fake.name() for _ in range(num_records)],
            "Candidate Email": [fake.email() for _ in range(num_records)],
            "Candidate Phone": [fake.phone_number() for _ in range(num_records)],
            "Father Name": [fake.name() for _ in range(num_records)],
            "DOB": [fake.date_of_birth(minimum_age=22, maximum_age=60).strftime('%Y-%m-%d') for _ in range(num_records)],
            "PAN Number": [f"ABCDE{random.randint(1000, 9999)}F" for _ in range(num_records)],
            "Aadhaar Number": [f"{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}" for _ in range(num_records)],
            "Address": [fake.address().replace('\n', ', ') for _ in range(num_records)],
            "Gender": [random.choice(['Male', 'Female']) for _ in range(num_records)],
            "BGV Areas": [random.choice(['Education', 'Employment', 'Address', 'Criminal']) for _ in range(num_records)],
        }
        df = pd.DataFrame(data)
       
        st.title("Candidate DataTable")
        st.divider()
        st.write(df)

        st.title("Search Student")
        st.divider()
        search_query = st.text_input("Search by Name or EMP Code", "")
        st.divider()
       
        filtered_df = df[df["Candidate Name"].str.contains(search_query, case=False) | 
                        df["EMP Code"].str.contains(search_query, case=False)]

       
        page_size = 5  # Number of rows per page
        total_pages = (len(filtered_df) - 1) // page_size + 1
       
        def display_buttons(df):
            for index, row in df.iterrows():
                col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
                print(row);
                with col1:
                    st.write(f"{row["Entity Code"]}-{row["EMP Code"]} ({row["Candidate Name"]})")  # Display row data or customize how to display it

                with col2:
                    if st.button(f"View Student {row["Entity Code"]}-{row["EMP Code"]}" ):
                        st.write(f"Button clicked for row {index}!")
                        # Here you can handle what happens when the button is clicked

        # Display buttons next to each row
        display_buttons(df)