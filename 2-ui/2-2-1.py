import streamlit as st

# Title of the app
st.title("Perimeter & Area Calculator")

# Input fields for width and length
w = st.number_input("Width:", min_value=0.0, step=0.1)
l = st.number_input("Length:", min_value=0.0, step=0.1)

# Buttons for "Calculate" and "Clear"
calculate = st.button("Calculate")
clear = st.button("Clear")

# Perform calculations when "Calculate" is clicked
if calculate:
    area = w * l
    perimeter = 2 * (l + w)
    st.write(f"Area: {area}, Perimeter: {perimeter}")

# Reset the inputs if "Clear" is clicked
if clear:
    w = 0.0
    l = 0.0
    st.write("Inputs cleared!")



