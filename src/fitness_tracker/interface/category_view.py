"""
Category user interface.
"""


class CategoryView:
    table = "category"

    def __init__(self, components: dict[str, any]) -> None:
        self.components = components
        self.model = components.get("category")
        self.controller = components.get("category_ctrl")(self.components)

    def new_category(self):
        category_name = input("Category Name: ").strip()
        new_id = self.controller.create_category(category_name)
        if new_id:
            print(f"Added category: {category_name} with id: {new_id}")

    def get_all_categories(self):
        categories = self.controller.read()
        "{'id': 1, 'name': 'test'}"
        return [categories[key] for key in categories]

    def view_categories(self):
        categories = self.controller.read(self.table)
        for attr in categories:
            print(f"{attr['id']}) {attr['name']}")

    def edit_category(self):
        pass

    def remove_category(self):
        pass
