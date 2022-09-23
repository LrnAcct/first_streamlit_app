import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents had a healthy dinner')
streamlit.header ('Breakfast Menu')
streamlit.text ('Omega 3 & Blueberry Oatmeal')
streamlit.text ('Kale, Spinach & Rocket Smoothie')
streamlit.text ('Hard-Boiled Free-Range Egg')

         
streamlit.title("My Mom's new healthy dinner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 OO Avocado Toast')


streamlit.title("Build Your Own Fruit Smoothie")
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#pre setting few fruits based on favourites
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

#display the table on the page
#streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index) ,['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on the page


streamlit.dataframe(fruits_to_show)
                                   
#DABW
#New Section to display fruityvice api response
streamlit.header ('Fruity Vice Advice')
#import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json()) # just writes the data to the screen


# take the json version of the response and normalize it
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

#fruit of choice
#fruit_choice=streamlit.text_input('What fruit would you like information about?', 'Kiwi')
try:        
fruit_choice=streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered', fruit_choice)

if not fruit_choice:         
         streamlit.error ("Please select a fruit to get information.")
else:
         fruityvice_response2=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
         streamlit.text(fruityvice_response2)
         fruityvice_normalized2=pandas.json_normalize(fruityvice_response2.json())
         streamlit.dataframe(fruityvice_normalized2)
         
except URLError as e:
         streamlit.error()

#Stop processing here 
streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_one_fruit = my_cur.fetchone()
streamlit.text(my_one_fruit)
my_fruit_list = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_fruit_list)

#fruit to add
fruit_add=streamlit.text_input('What fruit would you like to add?', 'Jackfruit')
streamlit.write('Thanks for adding ', fruit_add)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
