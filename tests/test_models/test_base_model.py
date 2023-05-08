#!/usr/bin/python3
"""
Test Case Model for BaseModel
"""
from models.base_model import BaseModel
import unittest
import uuid
import datetime


def issentence(s):
    """
    Tests if s is a sentence
    """
    return ((len(s) > 0) and
            (len(s.split(" ")) > 2))


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
        bm2 = BaseModel()
        self.assertIsInstance(bm1.id, uuid.UUID)
        self.assertFalse(bm1.id == bm2.id)

    def test_createdAt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime.datetime)

    def test_updatedAt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime.datetime)

    def test_strfunc(self):
        bm1 = BaseModel()
        self.assertTrue(issentence(bm1.__str__.__doc__))
        s = "[{2}] ({0}) {1}".format(bm1.id, bm1.__dict__,
                                     bm1.__class__.__name__)
        self.assertTrue(str(bm1) == s)

    def test_savefunc(self):
        bm1 = BaseModel()
        before = bm1.updated_at
        bm1.save()
        after = bm1.updated_at
        self.assertFalse(before == after)
        self.assertTrue(issentence(bm1.save.__doc__))

    def test_todict(self):
        bm1 = BaseModel()
        dict_rep = bm1.to_dict()
        self.assertTrue(issentence(bm1.to_dict.__doc__))
        self.assertIsInstance(dict_rep, dict)
        self.assertTrue("__class__" in dict_rep.keys())
        self.assertTrue("updated_at" in dict_rep.keys())
        self.assertTrue("created_at" in dict_rep.keys())
        self.assertTrue("id" in dict_rep.keys())
        self.assertIsInstance(dict_rep["updated_at"], str)
        self.assertIsInstance(dict_rep["created_at"], str)
