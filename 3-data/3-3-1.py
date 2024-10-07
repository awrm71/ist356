import pandas as pd
import streamlit as st
import requests
response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = response.json()

df_list=[]
for key in employees.keys():
    df = pd.DataFrame(employees[key])
    df['department'] = key
    df_list.append(df)

combine_df = pd.concat(df_list, ignore_index=True)

st.dataframe(combine_df)

