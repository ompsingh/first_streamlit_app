import pandas as pd
import streamlit
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My Parents New healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 My Fruit Smoothie 🥝🍇')
streamlit.text('1 🍌')
streamlit.text('10g 🍇 ')
streamlit.text('1 🥝')



my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =  my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)
#create the repatab;e code block called function
def get_fruityvice_data(this_fruit_choice):
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #streamlit.text(fruityvice_response.json()) #write data to screen
    # take the json version of the response and normalize it
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    back_from_function = get_fruityvice_data(fruit_choice) 
    # output it the screen as a table
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
# don't run anything past here while we troubleshoot
streamlit.stop()


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("Select * from fruit_load_list")
# #my_data_row = my_cur.fetchone()
# my_data_rows = my_cur.fetchall()
# #streamlit.text("Hello from Snowflake:")
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)
# # Allow the end user to add a new fruit to the list
# add_my_fruits = streamlit.text_input('What fruit would you like to add?','jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruits)
# my_cur.execute("insert into fruit_load_list values('from streamlit')")

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

