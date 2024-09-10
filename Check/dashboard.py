import streamlit as st
from Check.modules.AddCan import AddCandidate
from Check.modules.AllCandidate import allCandidate


css = """
.ef3psqc13 {
    border: none !important;
}
"""
page1 = "Candidate";

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def Dashboard():
    global page1  
        
    def Candidate():
        global page1 
        page1 = "Candidate"; 
        

    def Add():
        global page1  
        page1 = "AddCandidate"; 
        

    def status():
        global page1 
        page1 = "ActivityLogs"; 
        

    st.sidebar.text("Routes")
    
    st.sidebar.button("Candidate",use_container_width=True,on_click=Candidate)
    st.sidebar.button("Add Candidate / BGV",use_container_width=True,on_click=Add)
    st.sidebar.button("Activity Logs",use_container_width=True,on_click=status)


    if(page1 == "Candidate"):
        allCandidate()
    elif(page1 == "AddCandidate"):
        AddCandidate()
    elif(page1 == "ActivityLogs"):
        st.title("Activity Logs")
        for x in range(0,50):
            st.success("This is Log"+str(x));
    elif(page1 == "Dashboard"):
        st.write("This is From Dashboard")
       
    #home page

Dashboard()