"""
Exercise user interface.
"""


class ExerciseView:
    def __init__(self, components: dict[str, any]):
        self.components = components
        self.controller = components.get("exercise_ctrl")(self.components)

    def new_exercise(self):
        name = input("Exercise Name: ").strip()
        categories = self.controller.get_all_categories()
        invalid_id = True
        category_id = None
        while invalid_id:
            category_id = int(input("Enter category ID: "))
            if category_id not in categories.keys():
                print("Incorrect ID.")
            break
        new_id = self.controller.create_exercise(name, category_id)
        if new_id:
            print(f"Added exercise: {name} with id: {new_id}.")
            
    def view_exercises(self):
        pass
    
    def edit_exercise(self, exercise_id):
        pass
    
    def delete_exercise(self, exercise_id):
        pass
