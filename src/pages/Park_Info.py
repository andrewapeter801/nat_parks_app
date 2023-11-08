import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os
import numpy as np

# establish a filepath to 

filepath = os.path.join(Path(__file__).parents[1], 'nat_parks.csv')
filepath2 = os.path.join(Path(__file__).parents[1], 'new_clean_visits.csv')

df = pd.read_csv(filepath, low_memory=False)
df2 = pd.read_csv(filepath2, low_memory = False)

select = st.selectbox('Select the park to learn more',options=list(df['full_name'].unique()),placeholder='Select the Park')


df_filtered = df[df['full_name']==select]
st.write(f"Here's a description for {select}: {df_filtered['description'].values[0]}")
user_image_url = df_filtered['image_urls'].values[0].split(",")[0].replace("[", "").replace("'", "")
#image_desc = df_filtered['images'].values[0]
st.image(f"{user_image_url}",output_format="auto")


st.write(f"Weather information for {select}: {df_filtered['weather_info'].values[0]}")

park_code = df_filtered['park_code'].values[0]
df2_filtered = df2[df2['UnitCode']==park_code]

user_select = st.selectbox("What would you like to look at?", options = list(df2_filtered.select_dtypes(include = 'number')))

st.plotly_chart(px.bar(df2_filtered, x = 'Month', y = user_select, title = f"{user_select} in 2022 at {select}"))

st.markdown("", unsafe_allow_html = True)


st.plotly_chart(px.scatter_geo(df_filtered, lat='latitude', lon='longitude', locationmode='USA-states'))
st.plotly_chart(px.funnel_area(df_filtered,'designation'))




st.write('Planning a trip? Click the icon below!')


st.link_button('Directions!',(df_filtered['directions_url'].values[0]),type="secondary",disabled=False,use_container_width=False)











