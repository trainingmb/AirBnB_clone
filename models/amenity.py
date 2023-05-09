#!/usr/bin/python3
"""
Amenity class.
"""
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
	"""
	Doc string for the Amenity Class
	"""
	def __init__(self, *args, **kwargs):
		"""
		Public class attributes:
		name: string - empty string
		"""
		self.name = ""
		if (kwargs is not None) and (len(kwargs) > 0):
			super(Amenity, self).__init__(*args, **kwargs)
		else:
			super(Amenity, self).__init__()
