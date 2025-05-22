import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")
st.write("## This is a H2 Title!")
x = st.text_input("Movies","Star Wars")

if st.button("Click me"):
    st.write(f"Your favorite movies is {x}")

data = pd.read_csv("movies.csv")
st.write(data)

chart_data = pd.DataFrame(np.random.rand(20,3),columns=['a','b','c'])
st.bar_chart(chart_data)