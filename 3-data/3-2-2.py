# Write a streamlit to tabularize this JSON data, using `json_normalize`

# read the file using `requests` like the example

# [https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json](https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json)

# The final table should have these columns: `dept, age, firstname, lastname`

import streamlit as st
import pandas as pd
import requests

response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/master/json-samples/employees.json")
employees = response.json()
employees_df = pd.json_normalize(employees, record_path=["employees"], meta=["dept"])
st.dataframe(employees_df)