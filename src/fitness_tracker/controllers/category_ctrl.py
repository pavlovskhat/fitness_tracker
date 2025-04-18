"""
Category backend logic controller.
"""
from fitness_tracker.controllers.fitness_ctrl import FitnessCtrl


class CategoryCtrl(FitnessCtrl):
    table = "category"

    def __init__(self, components: dict[str, any]) -> None:
        super().__init__(components)
        self.model = components.get("category")

    def create_category(self, name: str) -> int | None:
        new_id = super().add_create(
            {"name": name},
            self.table
        )
        if new_id:
            self.model(category_name=name).set_id(new_id)
            return new_id
        return None
