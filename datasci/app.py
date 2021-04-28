import streamlit as st 

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache
def load_data():
    data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')
    data['week'] = data.year_week.apply(lambda x: convert(x))
    return data

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54 
    return year + int(week)
data = load_data()


st.title("Daily number of new reported COVID-19 cases and deaths")
st.text(" \n")

countries = data['country'].unique()
country_choice = st.sidebar.selectbox('Select the country:', countries)
country = data[data.country == country_choice]

st.write(f"The selected country is: {country_choice}")

fig = px.line(data_frame = country, x = 'week', y = 'cumulative_count', color = 'indicator', )

st.plotly_chart(fig)

