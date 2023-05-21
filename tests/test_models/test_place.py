#!/usr/bin/python3
"""
Test Case Model for Place
"""
from models.place import Place, BaseModel


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


class PlaceTestCase(unittest.TestCase):
    """
    Place for testing Place
    """
    def test_init(self):
        pl1 = Place()
        d = pl1.__dict__
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(existsandis("name", d, str))
        self.assertTrue(existsandis("state_id", d, str))
        self.assertTrue(existsandis("user_id", d, str))
        self.assertTrue(existsandis("description", d, str))
        self.assertTrue(existsandis("number_rooms", d, int))
        self.assertTrue(existsandis("number_bathrooms", d, int))
        self.assertTrue(existsandis("max_guest", d, int))
        self.assertTrue(existsandis("price_by_night", d, int))
        self.assertTrue(existsandis("latitude", d, float))
        self.assertTrue(existsandis("longtitude", d, float))
        self.assertTrue(existsandis("amenity_ids", d, list))

    def test_doc(self):
        pl1 = Place()
        self.assertIsInstance(pl1.__doc__, str)
        self.assertTrue(len(pl1.__doc__) > 0)
        self.assertTrue(issentence(pl1.__doc__))


if __name__ == '__main__':
    unittest.main()