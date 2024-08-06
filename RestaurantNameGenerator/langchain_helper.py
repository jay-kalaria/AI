import streamlit as st
import os
from langchain.llms import OpenAI
#from secret_key import openapi_key
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv

load_dotenv()
openapi_key = os.getenv("OPENAI_API_KEY")

#os.environ['OPENAI_API_KEY']= openapi_key
llm =OpenAI(temperature=0.7)


def generate_restaurant_name_and_items(cuisine):
  
  # Restaurant name
  prompt_template_name = PromptTemplate(
      input_variables = ['cuisine'],
      template = "I want to open {cuisine} food restaurant.Suggest a name"
  )
  name_chain=LLMChain(llm=llm , prompt=prompt_template_name , output_key="restaurant_name")

  # Menu items chain
  prompt_template_items = PromptTemplate(
      input_variables = ['restaurant_name'],
      template = "Suggest food items for {restaurant_name} .Return as comma seperated list ."
  )
  food_items_chain = LLMChain(llm=llm , prompt=prompt_template_items , output_key="menu_items")


  chain=SequentialChain(
      chains =[name_chain,food_items_chain],
      input_variables =['cuisine'],
      output_variables = ['restaurant_name','menu_items']
  )
  response = chain({'cuisine':cuisine})

  return response



if __name__ == "__main__":
  print(generate_restaurant_name_and_items("Italian"))


