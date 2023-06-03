import streamlit as st
from PIL import Image
st.title('Hi there; This app for EDA staff')
image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'
st.image(image_path)
# Display a message
st.write('This is a simple app for calculating square of numbers')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)




