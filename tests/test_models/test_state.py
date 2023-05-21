#!/usr/bin/python3
"""
Test Case Model for State
"""
from models.state import State, BaseModel


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


class StateTestCase(unittest.TestCase):
    """
    State for testing State
    """
    def test_init(self):
        st1 = State()
        d = st1.__dict__
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(existsandis("name", d, str))

    def test_doc(self):
        st1 = State()
        self.assertIsInstance(st1.__doc__, str)
        self.assertTrue(len(st1.__doc__) > 0)
        self.assertTrue(issentence(st1.__doc__))


if __name__ == '__main__':
    unittest.main()