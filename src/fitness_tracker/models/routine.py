"""
Routine model.
"""


class Routine:
    """
    Represents workout routines.
    """

    def __init__(self, name: str, exercise_id: int, routine_id=None):
        """
        Routine model constructor.

        :param name: Name of the routine.
        :param exercise_id: id of the exercise.
        :param routine_id: id of the routine.
        """
        self.name = name
        self.exercise_id = exercise_id
        self.routine_id = routine_id

    def __repr__(self):
        """
        String representation of the routine.
        """
        return f"({self.routine_id}) {self.name}"
