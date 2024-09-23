import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
customers = pd.read_csv(url)

view_option = st.radio("View:", ('Head', 'Tail'))

num_lines = st.number_input("Number of lines:", min_value=1, max_value=len(customers), value=5)

if view_option == 'Head':
    st.write(customers.head(num_lines))
else:
    st.write(customers.tail(num_lines))
