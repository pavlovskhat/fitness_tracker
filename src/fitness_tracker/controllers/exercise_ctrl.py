"""
Exercise backend logic controller.
"""
from typing import Any


class ExerciseCtrl:

    def __init__(self, database: Any, exercise_model: Any) -> None:
        self.database = database
        self.model = exercise_model

    def create_exercise(self, name: str, category_id: int) -> int | None:
        with self.database.connect() as db:
            exercise = self.model(name, category_id)
            context = {"name": name, "category_id": category_id}
            new_id = db.create("exercise", context)
            if new_id:
                exercise.exercise_id = new_id
                return new_id
            return None

    def update_exercise(
            self,
            data: dict[str, any],
            conditions: dict[str, any]
    ) -> int:
        with self.database.connect() as db:
            return db.update("exercise", data, conditions)

    def delete_exercise(self, conditions: dict[str, any]) -> int:
        with self.database.connect() as db:
            return db.delete("exercise", conditions)
