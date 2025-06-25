# Indian Recipe Book 

This is simple one Indian Recipe Book built for managing any loving recipe. To view, add, and save recipes for future.

## Features of Recipe Book

* **For Viewing Recipes** Can check by your saved recipes by dropdown menu.
* **Add New Recipes:** You can add new recipes with method of cooking and ingredients.
* **Stoarge Of Recipe:** Can be stored using JSON fILE format.
* **Overview Of Recipe :** You can view every recipe by names in section which can be expand down.
* **User Friendly Interface:** fair Streamlit-based UI.

## How to Start

1.  **Install Streamlit:**
    ```bash
    pip install streamlit
    ```


2.  **Run the App:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    streamlit run app.py
    ```

    This will automatically open the app in your web browser.

## Usage

1.  **Adding a New Recipe:** Find the "Add a New Recipe" section then put your name of new recipe, after that mention alll the ingredients accordingly by the recipes, also write cooking instructions.Finally click "Save New Recipe" button. Refresh the page to cehck your new recipe in the list.
2.  **Viewing Existing Recipes:** 
    * Select a recipe from the "Recipes Available " menu.
    * Tap "Show Recipe" button to display the full recipe details.
    * Recipe will show ingredients and steps for cooking.
3.  **Browsing All Recipes:**
    * Use "View All Recipe Names" in down section to see the list of recipes that are saved.
4.  **Storage of Data:**
The app uses a JSON file (recipes.json) to save data of all recipes with this way:

json{
  "Recipe Name": {
    "ingredients": "ingredient1, ingredient2, ingredient3",
    "steps": "Step 1\nStep 2\nStep 3"
  }
}

5.  **Structure Of Code:**
    * load_recipes(): Load data of recipe from JSON file
    * save_recipes(data): Saves the recipe data to JSON file
    * show_recipe(name, data): Displays recipe with formatting
    * main(): Main logic of app and UI components
6.  **Improvements:** 
    * fix the issue of case sensitivity
    


