#!/usr/bin/python3
"""
Test Case Model for city
"""
from models.city import City, BaseModel


def issentence(s):
    """
    Tests if s is a sentence
    """
    return ((len(s) > 0) and
            (len(s.split(" ")) > 2))


def existsandis(name, diction, tp):
    if (name not in diction.keys()):
        return False
    if not isinstance(diction[name] ,tp):
        return False
    return True


class CityTestCase(unittest.TestCase):
    """
    City for testing City
    """
    def test_init(self):
        ct1 = City()
        d = ct1.__dict__
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(existsandis("name", d, str))
        self.assertTrue(existsandis("state_id", d, str))

    def test_doc(self):
        ct1 = City()
        self.assertIsInstance(ct1.__doc__, str)
        self.assertTrue(len(ct1.__doc__) > 0)
        self.assertTrue(issentence(ct1.__doc__))


if __name__ == '__main__':
    unittest.main()