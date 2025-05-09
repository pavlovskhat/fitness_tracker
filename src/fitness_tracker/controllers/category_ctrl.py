"""
Category backend logic controller.
"""
from fitness_tracker.controllers.fitness_ctrl import FitnessCtrl


class CategoryCtrl(FitnessCtrl):
    table = "category"
    categories = []

    def __init__(self, components: dict[str, any]) -> None:
        super().__init__(components)
        self.model = components.get("category")
        self.refresh_categories()

    def create_category(self, name: str) -> int | None:
        new_id = super().create_request(
            {"name": name},
            self.table
        )
        if new_id:
            self.refresh_categories()
            return new_id
        return None

    def read_categories(self):
        return [
            [category.get_id(), category.get_name()]
            for category in self.categories
        ]

    def validate_category(self, selected_id):
        return selected_id in [category.get_id() for category in self.categories]

    def update_category(self, category_id, new_name):
        updated_category = self.model(new_name, category_id)
        self.categories.append(updated_category)
        super().update_request(self.table, updated_category)

    def refresh_categories(self):
        self.categories.clear()
        if super().read_request(self.table):
            self.categories = [
                self.model(
                    row["name"], row["id"]
                ) for row in super().read_request(self.table)
            ]

    def delete_category(self, selected_id):
        result = super().delete_request(selected_id, self.table)
        self.refresh_categories()
        return result
