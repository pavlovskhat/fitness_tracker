class FitnessModel:
	"""
	Application base model class.
	"""

	def __init__(self, name: str, _id=None):
		"""
		Base model constructor.

		:param name: Unique name label.
		:param _id: Primary key ID.
		"""
		self.name = name
		self._id = _id

	def set_id(self, new_id):
		"""
		Set new id for object.

		:param new_id: New id for object.
		"""
		self._id = new_id

	def __repr__(self):
		"""
		String representation of object.
		"""
		return f"({self._id}) {self.name}"