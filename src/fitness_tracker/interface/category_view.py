"""
Category user interface.
"""
from tabulate import tabulate


class CategoryView:
    labels = ["ID", "NAME"]

    def __init__(self, components: dict[str, any]) -> None:
        self.components = components
        self.controller = components.get("category_ctrl")(self.components)

    def new_category(self):
        category_name = input("Category Name: ").strip()
        new_id = self.controller.create_category(category_name)
        if new_id:
            print(f"Added category: {category_name} with id: {new_id}")

    def view_categories(self):
        print(tabulate(
            self.controller.read_categories(),
            headers=self.labels,
            tablefmt="fancy_grid"
        ))

    def edit_category(self):
        selected_id = int(input("Enter Category ID: "))
        if self.controller.validate_category(selected_id):
            new_name = input("New Name: ")
            self.controller.update_category(selected_id, new_name)

    def remove_category(self):
        selected_id = int(input("Enter Category ID: "))
        if self.controller.validate_category(selected_id):
            self.controller.delete_category(selected_id)
