import streamlit as st
import json

# -Data handling Functions-

# Functions to load data from JSON file
def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        
        return {}
    
    # Function to save data to JSON file
    def save_recipes(data):
        # Opens the file in "write" mode ('w'), which overwrites the file
        with open("recipes.json", "w") as file:
            # Dump the python dictionary 'data' into the file as a JSON string
            json.dump(data,file, indent=2)
