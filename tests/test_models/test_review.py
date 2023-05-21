#!/usr/bin/python3
"""
Test Case Model for Review
"""
from models.review import Review, BaseModel


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


class ReviewTestCase(unittest.TestCase):
    """
    Review for testing Review
    """
    def test_init(self):
        rv1 = Review()
        d = rv1.__dict__
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(existsandis("text", d, str))
        self.assertTrue(existsandis("place_id", d, str))
        self.assertTrue(existsandis("user_id", d, str))

    def test_doc(self):
        rv1 = Review()
        self.assertIsInstance(rv1.__doc__, str)
        self.assertTrue(len(rv1.__doc__) > 0)
        self.assertTrue(issentence(rv1.__doc__))


if __name__ == '__main__':
    unittest.main()