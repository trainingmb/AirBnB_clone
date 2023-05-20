#!/usr/bin/python3
"""
Test Case Model for Amenity
"""
from models.amenity import Amenity, BaseModel


def issentence(s):
    """
    Tests if s is a sentence
    """
    return ((len(s) > 0) and
            (len(s.split(" ")) > 2))


class AmenityTestCase(unittest.TestCase):
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
        am1 = Amenity()
        self.assertIsInstance(am1.__doc__, str)
        self.assertTrue(len(am1.__doc__) > 0)
        self.assertTrue(issentence(am1.__doc__))


if __name__ == '__main__':
    unittest.main()