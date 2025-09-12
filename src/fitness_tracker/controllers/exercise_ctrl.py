"""
Exercise backend logic controller.
"""
from typing import Any
from fitness_tracker.controllers.fitness_ctrl import FitnessCtrl


class ExerciseCtrl(FitnessCtrl):
    table = "exercise"
    exercises = []

    def __init__(self, components: dict[str, any]) -> None:
        super().__init__(components)
        self.model = components.get("exercise")
        self.refresh_exercises()

    def create_exercise(self, name: str, category_id: int) -> int | None:
        new_id = super().create_request({
                "name": name,
                "category_id": category_id
            })
        if new_id:
            self.refresh_exercises()
            return new_id
        return None

    def refresh_exercises(self):
        self.exercises.clear()
        if super().join_read_request(self.table):
            self.exercises = [
                self.model(
                    row["name"], row["title"], row["id"]
                ) for row in super().read_request(self.table)
            ]

    def read_exercises(self):
        return [
            [exercise.get_id(), exercise.get_name()]
            for exercise in self.exercises
        ]

    def validate_exercise(self, selected_id):
        return selected_id in [exercise.get_id() for exercise in self.exercises]

    def update_category(self, exercise_id, new_name):
        pass