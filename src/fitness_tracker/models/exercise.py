"""
Exercise model.
"""
from fitness_tracker.models.fitness_model import FitnessModel


class Exercise(FitnessModel):

    def __init__(self, exercise_name: str, category_id: int, exercise_id=None):
        super().__init__(exercise_name, category_id)
        self.category_id = category_id
        self.exercise_id = exercise_id

    def __repr__(self):
        return f"({self.exercise_id}) {self.exercise_name}"
