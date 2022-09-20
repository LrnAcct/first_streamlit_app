import streamlit
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
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my fruit list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
