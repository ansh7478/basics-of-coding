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

# - UI Display Functions -

# - Function to display the details of a single recipe
def show_recipe(name, data):
    st.subheader(name)
    st.markdown("### 🧂 Ingredients:")
    st.write(data[name]["Ingredients"])
    st.markdown("### 📝 Steps:")
    st.write(data[name]["Steps:"])

    # - Logic for Main Application -

    def main():
        # Set title and welcome message for app
        st.title("📖 Indian Recipe Book")
        st.markdown("welcome to the Indian Recipe Book🍲")

        # Load the recipes from JSON file at the start
        recipe = load_recipes()

        st.markdown("-")

        # - Section to View the Existing Recipes (Your Orginal Code) -
        st.header("🔍 View an Existing Recipe")

        # Get the recipe list names to show in the dropdown
        recipe_name = list(recipes.keys())

        # Only show the dropdown if there are available recipes
        if recipe_name:
            selected_recipe = st.selectbox( "Recipes Available:", recipe_names)

            # This is conditional statement: code inside runs only if the button is clicked
            if st.button("Show Recipe"):
                show_recipe(selected_recipe, recipes)
        else:
            st.info("There are no recipes yet. Add a new one below!")

        st.markdown("-")

        # - Section to Add a New Recipe (NEW FUNCTIONALLITY) -
        st.header("➕ Add a New Recipe")

        # Create text fields for the the user to input their new recipe details
        new_recipe_name = st.text_input("Recipe Name")
        new_recipe_ingredients = st.text_area("Ingredients (separated by commas)")
        new_recipe_steps = st.text_area("Steps (one per line)")

        # The button to trigger saving the new recipe
        if st.button("Save New Recipe"):
            # A nested conditional to check if all fields have filled out
            if new_recipe_name and new_recipe_ingredients and new_recipe_steps:
                # Add the new  recipe data to the main 'recipes' dictionary
                recipes[new_recipe_name] = {
                    "ingredients": new_recipe_ingredients,
                    "steps": new_recipe_steps
                }


    





