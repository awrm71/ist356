import pandas as pd
import streamlit as st

link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log'
webtraffic = pd.read_csv(link, sep=' ', skiprows=3, header=0)

webtraffic["time-taken"] = pd.to_numeric(webtraffic["time-taken"], errors='coerce')
webtraffic["sc-status"] = pd.to_numeric(webtraffic["sc-status"], errors='coerce')

filtered_data = webtraffic[(webtraffic["time-taken"] > 500) & (webtraffic["sc-status"] == 200)]

st.dataframe(filtered_data)

