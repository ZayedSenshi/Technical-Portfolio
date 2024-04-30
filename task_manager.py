"""
This script initializes a RecipeManager and a UserInterface, then runs the user interface.

Usage:
    python task_manager.py

This script serves as the entry point for the task manager application,
setting up the RecipeManager and UserInterface,
and then starting the user interface.
The RecipeManager handles the creation, display, update, and deletion of recipes,
while the UserInterface interacts with the user, taking inputs and communicating with the
RecipeManager accordingly.
"""


class FavouriteRecipes:
    """
    Representation of individual recipes

    Attributes:
        recipe_id (int): To keep track of created recipes
        title (str): Title of recipe
        ingredients (str): Ingredients required for recipe
        instructions (str): Instructions required to realise recipe.
    """

    def __init__(self, recipe_id, title, ingredients, instructions):
        self.recipe_id = recipe_id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions


class RecipeManager:
    """
    Manages a collection of recipes and encapsulates the CRUD operations.
    This class is responsible for the actual execution of CRUD.

    Attributes:
        recipes (list): A list of FavouriteRecipes instances
    """

    def __init__(self):
        """ Initialises the RecipeManager with an empty list of recipes.
        New recipes will be appended to this list
        """
        self.recipes = []

    def perform_create_recipe(self, title, ingredients, instructions):
        """
        Creates a new recipe and adds it to the collection.
        Prints the title of the recipe along with its ID
        and that it was successfully created.

        :param title : The title of the recipe
        :type title: str
        :param ingredients: The ingredients required for the recipe.
        :type ingredients: str
        :param instructions: The instructions for making the recipe.
        :type instructions: str
        :return: None. The method does not return any value
        :rtype: None
        """
        new_id = len(self.recipes) + 1
        new_recipe = FavouriteRecipes(new_id, title, ingredients, instructions)
        self.recipes.append(new_recipe)
        print(f"Recipe '{title}', with ID {new_id} created successfully!\n")

    def perform_display_recipes(self):
        """
        Displays the created recipes to user by iterating over
        the list containing the recipes

        :return: None. The method does not return any value
        :rtype: None
        """
        print("\033[1m" + "Favourite recipes: " + "\033[0m")
        for recipe in self.recipes:
            print(f"ID: {recipe.recipe_id}, Title: {recipe.title}, "
                  f"Ingredients: {recipe.ingredients}\n"
                  f"Instructions:\n{recipe.instructions}")
        print()

    def perform_update_recipe(self, recipe_id, new_title, new_ingredients, new_instructions):
        """
        Updates a recipe that has already been created.

        :param recipe_id : Integer used to identify relevant recipe
        :param new_title : An updated title of recipe
        :param new_ingredients : Updated ingredients
        :param new_instructions: Updated instructions
        :return: None. The method does not return any value.
        :rtype: None
        """
        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                if new_title is not None:
                    recipe.title = new_title
                if new_ingredients is not None:
                    recipe.ingredients = new_ingredients
                if new_instructions is not None:
                    recipe.instructions = new_instructions
                print(f"Recipe updated successfully!\n")
                return
        print(f"Recipe with ID: {recipe_id} not found.\n")

    def perform_delete_recipe(self, recipe_id):
        """
        Deletes a chosen recipe

        :param recipe_id: Integer used to identify relevant recipe
        :type recipe_id: int
        :return: None. The method does not return any value
        :rtype: None
        """
        for i, recipe in enumerate(self.recipes):
            if recipe.recipe_id == recipe_id:
                del self.recipes[i]
                print(f"Recipe with ID {recipe_id} deleted successfully!\n")
                return
        print(f"Recipe with ID {recipe_id} not found.\n")


class UserInterface:
    """
    Interacts with the user by taking in inputs
    and communicating with RecipeManager accordingly.

    Attributes:
        recipe_manager: reference to an instance of RecipeManager
    """

    def __init__(self, recipe_manager):
        """
        :param recipe_manager: Allows operations to be performed
        with regard to managing recipes.
        """
        self.recipe_manager = recipe_manager

    def run(self):
        """
        Responsible for taking user inputs pertaining to the menu.

        :return: None. The method does not return any value
        :rtype: None
        """

        while True:
            try:
                user_choice = self.display_menu_and_get_choice()
                if user_choice == 1:
                    self.create_recipe()
                elif user_choice == 2:
                    self.display_recipes()
                elif user_choice == 3:
                    self.update_recipe()
                elif user_choice == 4:
                    self.delete_recipe()
                elif user_choice == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please ensure you enter the relevant number "
                      "to represent your choice.")

    @staticmethod
    def display_menu_and_get_choice():
        """
        Displays the main menu to the user and retrieves their choice.

        This method presents the user with a list of options to choose from,
        including creating a recipe, displaying recipes, updating a recipe,
        deleting a recipe, and exiting the application. It then prompts the user
        to enter their choice and returns the selected option as an integer.

        :return: An integer representing the user's choice.
        :rtype: int
        """
        print(f''' Would you like to:
            1. Create a favourite recipe
            2. Display favourite recipes
            3. Update a favourite recipe
            4. Delete a favourite recipe
            5. Exit

            Enter selection: ''')
        return int(input())

    def create_recipe(self):
        """
        Prompts the user to input details for a new recipe and adds it to the collection.

        This method interacts with the user to collect the title, ingredients, and instructions
        for a new recipe. It ensures the inputs are not blank by calling on
        get_non_blank_input_and_or_multiline.
        It then calls the `perform_create_recipe` method of the `RecipeManager`
        to add the new recipe to the collection.
        :return: None. The method does not return any value.
        :rtype: None
        """
        title = self.get_non_blank_input_and_or_multiline("Enter recipe title: ", "Please ensure you enter a title")
        ingredients = self.get_non_blank_input_and_or_multiline("Enter ingredients: ",
                                                                "Please ensure you enter ingredients.")
        instructions = self.get_non_blank_input_and_or_multiline('''
        Please enter your instructions line by line.
        Once you are done, enter an empty line to finish: 
        Example: 
        1. Chop onions
        2. Peel potatoes
        ''', "Please ensure you enter instructions", multiline=True)
        self.recipe_manager.perform_create_recipe(title, ingredients, instructions)

    def display_recipes(self):
        """
        Displays all the recipes stored in the RecipeManager to the user.

        This method checks if there are any recipes in the RecipeManager.
        If recipes are present, it calls the `perform_display_recipes` method of the RecipeManager
        to display each recipe's details, including its ID, title, ingredients, and instructions.
        If no recipes are found, it informs the user accordingly.

        :return: None. The method does not return any value.
        :rtype: None
        """
        if not self.recipe_manager.recipes:
            print("There are no recipes to display")
            return
        self.recipe_manager.perform_display_recipes()

    def update_recipe(self):
        """
        Prompts the user to update details of an existing recipe.

        This method first checks if there are any recipes in the RecipeManager.
        If recipes are present, it prompts the user to enter the ID
        of the recipe they wish to update.
        It then asks the user whether they want to change the title, ingredients, or instructions
        of the recipe. Based on the user's choices, it collects the new details
        and calls the `perform_update_recipe` method
        of the RecipeManager to update the recipe.
        If the recipe ID is not found or no recipes are present,
        it informs the user.

        :return: None. The method does not return any value.
        :rtype: None
        """
        if not self.recipe_manager.recipes:
            print("There are no recipes to update")
            return
        try:
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            if not any(recipe.recipe_id == recipe_id for recipe in self.recipe_manager.recipes):
                print(f"Recipe with ID: {recipe_id} not found.\n")
                return

            title_change = self.get_yes_no_input(
                "Would you like to change the title? (yes/no): "
            )
            new_title = (
                self.get_non_blank_input_and_or_multiline(
                    "Enter a new title: ",
                    "Please input a valid title."
                )
                if title_change == "yes"
                else None
            )
            ingredients_change = self.get_yes_no_input(
                "Would you like to change the ingredients? (yes/no): "
            )
            new_ingredients = (self.get_non_blank_input_and_or_multiline
                               ("Enter new ingredients: ",
                                "Please input a valid title.")) \
                if ingredients_change == "yes" else None

            instructions_change = (self.get_yes_no_input
                                   ("Would you like to change the instructions? (yes/no): "))
            new_instructions = self.get_non_blank_input_and_or_multiline(
                "Enter new instructions line by line."
                " Enter an empty line to finish updating your instructions: ",
                "Please ensure you enter instructions", multiline=True) \
                if instructions_change == "yes" else None

            self.recipe_manager.perform_update_recipe(recipe_id, new_title, new_ingredients, new_instructions)
        except ValueError:
            print("Please enter a valid recipe ID.")

    def delete_recipe(self):
        """
        Prompts the user to delete a recipe.

        This method first checks if there are any recipes in the RecipeManager.
        If there are not it returns None and breaks the loop. If the list is
        not empty then the user is prompted to enter the recipe ID.
        If a recipe ID is entered which exists, the user is prompted with a yes or no input
        as a means of double-checking if they want to delete the recipe. If they choose
        yes then it calls `perform_delete_recipe` method of the RecipeManager
        to remove the recipe from the collection.
        If the recipe ID is not found, it informs the user.

        :return: None. The method does not return any value.
        :rtype: None
        """
        if not self.recipe_manager.recipes:
            print("There are no recipes to delete")
            return
        while True:
            try:
                recipe_id_choice = int(input("Enter the ID of the recipe to delete: "))
                found = False
                for recipe in self.recipe_manager.recipes:
                    if recipe.recipe_id == recipe_id_choice:
                        found = True
                        break
                if not found:
                    print(f"Recipe with ID {recipe_id_choice} does not exist")
                    break  # Exit the loop if the ID is not found
                confirm_deletion = self.get_yes_no_input("Are you sure you want to delete this recipe? (yes/no): ")
                if confirm_deletion == "yes":
                    self.recipe_manager.perform_delete_recipe(recipe_id_choice)
                    break
                else:
                    print("You have decided to keep the recipe")
                    break
            except ValueError:
                print("Please enter a valid recipe ID.")

    @staticmethod
    def get_yes_no_input(prompt_to_user):
        """
        Prompts the user for a yes or no input.

        This method displays a prompt to the user and waits for their input.
        It then checks if the input is 'yes' or 'no',
        returning True if 'yes' is entered and False if 'no' is entered.
        If the input is not recognized, it prompts the user again until a valid input
        is received.

        :param prompt_to_user: The message to display to the user.
        :type prompt_to_user: str
        :return: True if the user enters 'yes', False if 'no'.
        :rtype: bool
        """
        while True:
            response = input(prompt_to_user).lower()
            if response in ['yes', 'no']:
                return response
            else:
                print("Please enter 'yes' or 'no'.")

    @staticmethod
    def get_non_blank_input_and_or_multiline(instructions_to_user, error_message, multiline=False):
        """
        Prompts the user for input and returns the input as a string, ensuring it is not empty.

        This method displays a prompt to the user and waits for their input.
        It then checks if the input is not blank.
        If the input is blank, it prompts the user again until a non-blank input is received.
        If the `multiline` parameter is set to True, the method
        allows for multi-line input, which is useful for capturing detailed text inputs.

        :param instructions_to_user: The prompt message to display to the user.
        :type instructions_to_user: str
        :param error_message: The error message to display if the input is blank.
        :type error_message: str
        :param multiline: If True, allows for multiple lines of input.
        :type multiline: bool
        :return: The user's input as a string.
        :rtype: str
        """
        while True:
            # if multiline is True
            if multiline:
                print(instructions_to_user)
                # initiate empty list to store multiline inputs
                lines = []
                while True:
                    line = input()
                    # if the line isn't empty, add to lines list
                    if line:
                        lines.append(line)
                    else:
                        break
                        # string from user is joined together
                        # but separated by newline characters
                        # and stored in user_input
                user_input = '\n'.join(lines)
            else:
                # If multiline is false (not required),
                # then relevant instructions are displayed for input
                user_input = input(instructions_to_user)

            if user_input.strip() != "":
                return user_input
            else:
                print(error_message)


if __name__ == "__main__":
    """
    Main entry point for the application.

    This block initializes the RecipeManager and UserInterface, then starts the user interface.
    """
    recipe_manager = RecipeManager()
    user_interface = UserInterface(recipe_manager)
    user_interface.run()
