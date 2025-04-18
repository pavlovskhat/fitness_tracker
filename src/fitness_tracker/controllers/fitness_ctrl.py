"""
Application base controller.
"""
from fitness_tracker.settings.settings import Constants


class FitnessCtrl:
	"""
	Base controller class.
	"""

	def __init__(self, components: dict[str, any]) -> None:
		self.components = components
		self.database = components.get("database")(Constants.DB_PATH)

	def add_create(self, context: dict, table: str) -> int | None:
		return self.database.create(table, context)

	def read(self, table: str) -> list[dict[str, any]]:
		return self.database.read(table)

	def update(self, data: str, conditions: dict[str, any], table: str) -> int:
		return self.database.update(table, data, conditions)

	def delete(self, conditions: dict[str, any], table: str) -> int:
		return self.database.delete(table, conditions)
