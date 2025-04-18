"""
Goal model.
"""


class Goal:
    """
    Represents fitness or weight loss goals.
    """

    def __init__(self, goal_name: str, goal_value: int, goal_id=None):
        """
        Goal model constructor.

        :param goal_name: Name of the goal.
        :param goal_value: Value of the goal.
        :param goal_id: id of the goal.
        """
        self.goal_name = goal_name
        self.goal_value = goal_value
        self.goal_id = goal_id

    def __repr__(self):
        """
        Return string representation of Goal model.
        """
        return f"({self.goal_id}) {self.goal_name}"
