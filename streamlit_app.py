
import streamlit
streamlit.title('My Parents New healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 My Fruit Smoothie 🥝🍇')
streamlit.text('1 🍌')
streamlit.text('10g 🍇 ')
streamlit.text('1 🥝')


import pandas as pd
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
