import streamlit as st

st.title("Add a Number")

N = st.number_input("Input a number to add", min_value=0.0, step=1.0)

if 'total' not in st.session_state:
    st.session_state.total = 0.0
    st.session_state.history = []

calc = st.button("Calculate total")
clear = st.button('Clear')

if calc:
    st.session_state.total += N
    st.session_state.history.append(N)
    st.write(f"total calculated = {st.session_state.total}")
    st.write("history:", st.session_state.history)

if clear:
    st.session_state.total = 0.0
    st.session_state.history = []
    st.write(f"total calculated = {st.session_state.total}")
    st.write("history:", st.session_state.history)