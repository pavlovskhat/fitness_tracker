"""
Exercise model.
"""
from fitness_tracker.models.fitness_model import FitnessModel


class Exercise(FitnessModel):
    """
    Represents a single exercise.
    """

    def __init__(self, name: str, category_id: int, exercise_id=None):
        """
        Exercise model constructor.

        :param name: Name of the exercise.
        :param category_id: Category id of the exercise.
        :param exercise_id: id of the exercise.
        """
        self.name = name
        self.category_id = category_id
        self.exercise_id = exercise_id

    def __repr__(self):
        """
        String representation of the Exercise.
        """
        return f"({self.exercise_id}) {self.name}"
