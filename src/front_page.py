import streamlit as st
import base64

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://unsplash.com/photos/low-angle-photography-of-green-trees-during-daytime-UDTQ0737wu0")
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Bonfire-129 Capstone Project")
st.text("Created by: Andrew Peterson")
st.markdown("---")
st.text('''My application utilizes Pandas, Streamlit, MongoDB, Tableau, and Python to create 
        an info deck from the National Parks Service API!''')

