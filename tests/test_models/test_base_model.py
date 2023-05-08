#!/usr/bin/python3
"""
Test Case Model for BaseModel
"""
from models.base_model import BaseModel
import unittest
import uuid
import datetime

class BaseModelTestCase(unittest.TestCase):
	"""
	Class for testing BaseModel
	"""
	def test_doc(self):
		bm1 = BaseModel()
		self.assertIsInstance(bm1.__doc__, str)
		self.assertTrue(len(bm1.__doc__) > 0)

	def test_id(self):
		bm1 = BaseModel()
		self.assertIsInstance(bm1.id, uuid.UUID)

	def test_createdAt(self):
		bm1 = BaseModel()
		self.assertIsInstance(bm1.created_at, datetime.datetime)

	def test_updateedAt(self):
		bm1 = BaseModel()
		self.assertIsInstance(bm1.updated_at, datetime.datetime)