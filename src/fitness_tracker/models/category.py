"""
Category table model.
"""
from fitness_tracker.models.fitness_model import FitnessModel


class Category(FitnessModel):
    """
    Represents an exercise category.
    """

    def __init__(self, category_name: str, category_id=None):
        """
        Category model constructor.

        :param category_name: Category unique name.
        :param category_id: Primary key ID.
        """
        super().__init__(category_name, category_id)
