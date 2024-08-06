import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pick a cuisine" ,("Indian","Italian","Mexican","Arabic","American"))

# def generate_restaurant_name_and_items(cuisine):
#   return{
#     'restaurant_name':'Curry delight',
#     'menu_items':'samosa,paneer tikka'
#   }

if cuisine :
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)

  st.header(response['restaurant_name'].strip())
  menu_items = response['menu_items'].strip().split(",")
  st.write("**Menu Items**")
  for item in menu_items:
    st.write("-",item)