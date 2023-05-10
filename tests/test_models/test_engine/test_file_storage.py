#!/usr/bin/python3
"""
Test Case Model for FileStorage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


def issentence(s):
    """
    Tests if s is a sentence
    """
    return ((len(s) > 0) and
            (len(s.split(" ")) > 2))



class FileStorageTestCase(unittest.TestCase):
	"""
	Class for testing the FileStorage class
	"""
	def test_classdocstring(self):
		self.assertTrue(issentence(FileStorage.__doc__))

	def test_all(self):
		fs = FileStorage()
		dictObjts = fs.all()
		self.assertIsInstance(dictObjts, dict)
		self.assertTrue(issentence(fs.all.__doc__))

	def test_new(self):
		fs = FileStorage()
		bm1 = BaseModel()
		fs.new(bm1)
		key = "{}.{}".format(bm1.__class__.__name__,
                             bm1.id)

		self.assertTrue(issentence(fs.new.__doc__))
