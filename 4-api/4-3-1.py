'''
Let's write an LLM-based spellchecker!

The spellchecker should take some text as input and return the misspelled works along with suggestions for the correct spellings. 

Make the inputs, then create a suitable prompt for the LLM. 
'''

import pandas as pd
import requests 
import streamlit as st

def openai_complete(prompt):
    url = 'https://cent.ischool-iot.net/api/openai/generate'
    params= {'temperature':0}
    headers = {'X-API-KEY': 'bdde3a191448e3810f521061'}
    data = {'query' : prompt}
    response = requests.post(url, headers=headers, data=data, params=params)
    response.raise_for_status()
    return response.json()

def spell_check(text):
    prompt = "Spell check the following text: \n"
    prompt += text + '\n'
    prompt += 'for each misspelled word, provide one suggestion to correct the spelling \n'
    prompt += 'return these as a list of dictionary in JSON format \n'
    response = openai_complete(prompt)
    return response

st.title('Spellchecker')
text = st.text_area('Enter some text to spellcheck:')
response = spell_check(text)
st.write(response)
