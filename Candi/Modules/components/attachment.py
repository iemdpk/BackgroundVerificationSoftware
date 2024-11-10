import streamlit as st
import random
def document_upload():
    st.header("Document Upload")

    # File upload fields
    pan_attachment = st.file_uploader("PAN Attachment", type=["pdf", "jpg", "jpeg", "png"])
    passport = st.file_uploader("Passport", type=["pdf", "jpg", "jpeg", "png"])
    aadhar = st.file_uploader("Aadhar", type=["pdf", "jpg", "jpeg", "png"])
    address_proof_current = st.file_uploader("Address Proof (Current Address)", type=["pdf", "jpg", "jpeg", "png"])
    address_proof_permanent = st.file_uploader("Address Proof (Permanent Address)", type=["pdf", "jpg", "jpeg", "png"])

    # Note
    st.write("**Note:** Please attach Ration Card / Passport / Landline Telephone Bill / Electricity Bill / Rent Agreement to be verified.")

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
        st.success("Documents uploaded successfully.")

# Run the document_upload function
if __name__ == "__main__":
    document_upload()
