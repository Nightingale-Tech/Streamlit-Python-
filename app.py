import streamlit as st

st.title("Welcome to My First App ")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}, welcome! ")

age = st.number_input("Enter your age:")

if age:
    st.write(f"Nightingale is {age} years old.")  

city = st.text_input( "Enter your city") 

if city:
    st.write(f"Nightingale lives in {city}.")