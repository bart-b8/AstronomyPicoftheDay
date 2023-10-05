import requests
import streamlit as st

url = ("https://api.nasa.gov/planetary/apod?"
       "api_key="+st.secrets["API_key"])

response = requests.get(url)
content = response.json()

st.title("Astonomy Pic of the Day")

st.image(content['hdurl'])
st.header(content['title'])
st.write(content['explanation'])
if (content['copyright']):
    st.write("Credits & copyright: " + content['copyright'])

# st.write(response.json())
