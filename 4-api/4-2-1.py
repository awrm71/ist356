import requests
import streamlit as st
import pandas as pd

def extract_entities(text: str) -> dict:
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    data = {"text": text}
    headers = {'X-API-KEY': 'bdde3a191448e3810f521061'
    }
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

text = st.text_area('Enter some text')
if text:
    results = extract_entities(text)
    entities = results['results']['documents'][0]['entities']
    df = pd.DataFrame(entities)
    st.dataframe(df)