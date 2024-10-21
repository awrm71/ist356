import requests
import streamlit as st
from time import sleep
''' GEOCODE
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=Syracuse%2C%20NY' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: bdde3a191448e3810f521061'
'''


''' WEATHER
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial&lon=78&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: bdde3a191448e3810f521061'
'''

st.title('Weather')
location = st.text_input('Enter a location')
if st.button('Get Weather'):
    with st.spinner('Getting Weather...'):
        sleep(2)
        url = "https://cent.ischool-iot.net/api/google/geocode"
        querystring = {"location": location}
        headers = {'X-API-KEY': 'bdde3a191448e3810f521061'}
        response = requests.get(url, params=querystring, headers=headers)
        response.raise_for_status()
        geocode = response.json()
        lon = geocode['results'][0]['geometry']['location']['lng']
        lat = geocode['results'][0]['geometry']['location']['lat']

        url = "https://cent.ischool-iot.net/api/weather/current"
        querystring = {"units": "imperial", "lon": lon, "lat": lat}
        response = requests.get(url, params=querystring, headers=headers)
        response.raise_for_status()
        weather = response.json()
        temp = weather['current']['temperature_2m']
        st.metric('Temperature', temp, '°F')   