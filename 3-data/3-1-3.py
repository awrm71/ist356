import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
customers = pd.read_csv(url)

gender_select = st.radio("Gender:", ('M', 'F'))

cols = st.multiselect("select columns:", customers.columns)
gender_index = customers['Gender'] == gender_select

st.dataframe(customers[gender_index][cols])
