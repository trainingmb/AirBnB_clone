#!/usr/bin/python3
"""
Test Case Model for Amenity
"""
from models.amenity import Amenity
from models.base_model import BaseModel


def issentence(s):
    """
    Tests if s is a sentence
    """
    return ((len(s) > 0) and
            (len(s.split(" ")) > 2))


class BaseModelTestCase(unittest.TestCase):
    """
    Amenity for testing BaseModel
    """
    def test_init(self):
        am1 = Amenity()
        d = am1.__dict__
        self.assertTrue(issubclass(Amenity,BaseModel))
        self.assertTrue("name" in d.keys())
        self.assertIsInstance(am1.name, str)
        self.assertTrue(am1.len == 0)

    def test_doc(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.__doc__, str)
        self.assertTrue(len(bm1.__doc__) > 0)
        self.assertTrue(issentence(bm1.__doc__))
