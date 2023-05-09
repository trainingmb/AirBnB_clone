#!/usr/bin/python3
"""
State class.
"""
from models import storage
from models.base_model import BaseModel



class State(BaseModel):
	"""
	Doc string for the State Class
	"""
	def __init__(self, *args, **kwargs):
		"""
		Init for State with a public class
		attribute: name<string
		"""
		self.name = ""
		if (kwargs is not None) and (len(kwargs) > 0):
			super(State, self).__init__(*args, **kwargs)
		else:
			super(State, self).__init__()
