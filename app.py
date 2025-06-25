import streamlit as st
import json

# This functions help to load data from JSON file
def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        
        return {}
    
    # This function helps to save data to JSON file
def save_recipes(data):
        
        # Opens the file in "write" mode ('w'), which will overwrites the file
        with open("recipes.json", "w") as file:
            # Dump the python dictionary with 'data' into the file as a JSON string
            json.dump(data,file, indent=2)

# UI Functions 

# Single recipe will be displayed with this function

def show_recipe(name, data):
    st.header(name)
    
    if "Ingredients" in data[name]:
        st.subheader("Ingredients")
        st.write(data[name]["Ingredients"])
    else:
        st.subheader("Ingredients")
        st.write("No ingredients listed for this recipe.")
    
    if "Steps" in data[name]:
        st.subheader("Steps")
        st.write(data[name]["Steps"])
    else:
        st.subheader("Steps")
        st.write("No steps provided for this recipe.")


    #  This will be help for logic in Main Application 

def main():
        
        # We will set title and welcome message for users in the app
        st.title("Indian Recipe Book")
        st.markdown("welcome to the Indian Recipe Book")

        # Then load the recipes from JSON file at the start
        recipe = load_recipes()

        st.markdown("-")

        # Existing recipes will be displayed with this section 
        st.header("View an Existing Recipe")

        # Get the names of recipe list to show in the dropdown menu
        recipe_name = list(recipe.keys())

        #  If there are available recipes then only it will show the dropdown
        if recipe_name:
            selected_recipe = st.selectbox( "Recipes Available:", recipe_name)

            # This will run only run if the button will be clicked because this is conditional statement 
            if st.button("Show Recipe"):
                show_recipe(selected_recipe, recipe)
        else:
            st.info("There are no recipes yet. Add a new one below!")

        st.markdown("-")

        # This is the section to add a New Recipe 
        st.header(" Add a New Recipe")

        # Create text fields for the the user to input their new recipe details
        new_recipe_name = st.text_input("Recipe Name")
        new_recipe_ingredients = st.text_area("Ingredients (separated by commas)")
        new_recipe_steps = st.text_area("Steps (one per line)")

        # The button to trigger saving the new recipe
        if st.button("Save New Recipe"):
            # A nested conditional to check if all fields have filled out
            if new_recipe_name and new_recipe_ingredients and new_recipe_steps:
                # Add the new  recipe data to the main 'recipes' dictionary
                recipe[new_recipe_name] = {
                    "ingredients": new_recipe_ingredients,
                    "steps": new_recipe_steps
                }

                # Call the save_recipes functipn to write the updated dictionary to the file
                save_recipes(recipe)

                # Show a success message to the user
                st.success(f"Recipe '{new_recipe_name}' saved successfully!")
                st.info("Refresh the page to see the new recipe in the dropdown list.")
            else:
                # Show an error message if any field is empty
                st.error("Please fill in the all fields to save the recipe.")

        st.markdown("-")

        # This will display all recipe names in an expandable section
        with st.expander("View All Recipe Names"):
            # Reload the recipe name in case a new one was just added
            updated_recipe_name = list(load_recipes(). keys())

            # Check if the list is not empty
            if updated_recipe_name:
                # This is a loop will help it iterates all the names through the list
                for i, name in enumerate(updated_recipe_name, 1):
                    st.write(f"{i}. {name}")
            else:
                st.write("No recipes have been saved yet.")


#  When the script is executed this fucntion will ensures that it runs
if __name__ == "__main__":
    main()




    





