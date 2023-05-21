#!/usr/bin/python3
"""
Test Case Model for User
"""
from models.user import User, BaseModel


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


class UserTestCase(unittest.TestCase):
    """
    User for testing User
    """
    def test_init(self):
        us1 = User()
        d = us1.__dict__
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(existsandis("name", d, str))

    def test_doc(self):
        us1 = User()
        self.assertIsInstance(us1.__doc__, str)
        self.assertTrue(len(us1.__doc__) > 0)
        self.assertTrue(issentence(us1.__doc__))


if __name__ == '__main__':
    unittest.main()