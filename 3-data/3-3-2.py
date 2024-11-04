import pandas as pd
import streamlit as st
import requests

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart"

customers = pd.read_csv(base + '/customers.csv')
st.write('Customers')
months = ['jan', 'feb', 'mar', 'apr']
pd.DataFrame(customers)
months_df = []
for month in months:
    month_df= pd.read_csv(base + f"/purchases-{month}.csv")
    month_df["month"]=month
    months_df.append(month_df)

purchases = pd.concat(months_df)
combined = pd.merge(customers, purchases, on='customer_id', how='outer').sort_values(by='month')
selected_month = st.selectbox('Select a box', months)
filtered = combined[combined['month'] == selected_month]
no_purchase = combined[combined['order_id'].isna()]

st.dataframe(filtered)