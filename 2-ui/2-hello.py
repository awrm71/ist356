import streamlit as st
#build
st.title("Saying Hello.")
name = st.text_input("Enter a name!")
#evaluate
if name:
    st.write(f"Hello, {name}!")
