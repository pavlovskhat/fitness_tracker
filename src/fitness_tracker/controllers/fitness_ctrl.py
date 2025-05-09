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

	def create_request(self, context: dict, table: str) -> int | None:
		return self.database.create(table, context)

	def read_request(self, table: str) -> list[dict[str, any]]:
		return self.database.read(table)

	def update_request(self, table, category: any) -> int:
		return self.database.update(
			table,
			{"name": category.get_name()},
			{"id": category.get_id()}
		)

	def delete_request(self, category_id: int, table: str) -> int:
		return self.database.delete(table, {"id": category_id})
