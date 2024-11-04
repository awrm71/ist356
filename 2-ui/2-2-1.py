import streamlit as st

st.title("Perimeter & Area Calculator")

w = st.number_input("Width:", min_value=0.0, step=0.1)
l = st.number_input("Length:", min_value=0.0, step=0.1)

calculate = st.button("Calculate")
clear = st.button("Clear")

if calculate:
    area = w * l
    perimeter = 2 * (l + w)
    st.write(f"Area: {area}, Perimeter: {perimeter}")

if clear:
    w = 0.0
    l = 0.0
    st.write("Inputs cleared!")





