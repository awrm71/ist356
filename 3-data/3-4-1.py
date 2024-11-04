import pandas as pd
import streamlit as st

from check_functions import clean_currency, detect_whale

# load the checks df
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv"
df = pd.read_csv(url)

df['total_amount _of_check_cleaned'] = df['total amount of check'].apply(clean_currency)

df['gratuity_cleaned'] = df['gratuity'].apply(clean_currency)

df['items_per_person'] = df['total items on check'] / df['party size']

df['tip_percentage'] = df['gratuity_cleaned'] / df['total_amount _of_check_cleaned'] 

df['whale'] = df.apply(lambda row: detect_whale(row['items_per_person'], row['price_per_person'], ipp_75, ppp_75), axis=1)

st.dataframe(df)

st.dataframe(df.describe())