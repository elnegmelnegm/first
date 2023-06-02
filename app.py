import streamlit as st
st.title('Hello World')

# Display a message
st.write('This is a simple Streamlit app for calculating square of numbers')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)




