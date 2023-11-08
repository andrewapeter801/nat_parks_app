import streamlit as st

st.header("National Park's Application Summary")
st.text("""
        The purpose of this application is to create an application using the
        National Park's Api. The first steps to do this was pulling the data,
        cleaning the data, and pushing the data to MongoDB. 

        In Python, I was able to create parameters for a Streamlit application. 
        I was able to create a 'Park Info' page which holds all the information from 
        a particular park, which included; a picture, destination statistics, and 
        a 'button' link to take the user to a NPS page with directions.

        Next steps, learn more about how to retrieve data in deeply nested in a cell. 
        I would also like to learn how to get Tableau and R linked into Streamlit.


        """)

st.text("""
        
        """)
if st.checkbox("Celebration time?"):
    st.balloons()
st.image('https://logos-download.com/wp-content/uploads/2016/10/Python_logo_wordmark-700x203.png')

st.text("Thank you for visiting my Streamlit app!")